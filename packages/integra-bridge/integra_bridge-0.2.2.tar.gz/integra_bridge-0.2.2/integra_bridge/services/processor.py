import traceback

import orjson
import xmltodict
from pydantic import ValidationError

from integra_bridge.adapters import ProcessorAdapter
from fastapi import HTTPException, Request
from starlette import status

from integra_bridge.dto import Exchange
from integra_bridge.dto.responces.validation import ValidationResponse
from integra_bridge.entity.processed_components import ProcessedComponents
from integra_bridge.entity.processor import Processor


class ProcessorHandler:
    @classmethod
    async def execute(cls, request: Request, processor_title: str) -> Exchange:
        processor_adapter = await cls.__get_processor_by_title(processor_title)

        if isinstance(request, Request):
            # Дисериализация входных данных
            try:
                exchange = await request.json()
            except Exception:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                    detail="Input body is not JSON serializable")
        else:
            exchange = request

        # Дисериализация exchange в python объекты
        exchange_data = await ProcessorHandler.exchange_deserialization(exchange)

        processed_components = ProcessedComponents(
            body=exchange_data['inputBody'],
            input_headers=exchange_data['inputHeaders'],
            headers=exchange_data['headers'],
            context=exchange_data['context'],
            params=exchange_data['params'],
        )
        try:
            processed_exchange_components = await processor_adapter.execute(processed_components)
        except Exception as e:
            exception = traceback.format_exc()
            exception_lines = exception.splitlines()[3:]
            formatted_exception = "\n".join(exception_lines).strip()
            formatted_exception = formatted_exception[2:]
            exchange["exception"] = str(e)
            exchange['stackTrace'] = formatted_exception
        else:
            context_exists = True if exchange_data['context_exists'] or processed_exchange_components.context else False
            processed_exchange = await ProcessorHandler.exchange_serialization(
                exchange=exchange,
                context_exists=context_exists,
                body=processed_exchange_components.body,
                context=processed_exchange_components.context,
                input_headers=processed_exchange_components.input_headers,
                headers=processed_exchange_components.headers,
            )
            try:
                exchange = Exchange(**processed_exchange)
            except ValidationError as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        return exchange

    @classmethod
    async def validate(cls, processor: Processor, title: str) -> ValidationResponse:
        try:
            processor_adapter = await cls.__get_processor_by_title(title)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        return await processor_adapter.validate(processor)

    @classmethod
    async def __get_processor_by_title(cls, title: str) -> ProcessorAdapter:
        from integra_bridge.common.enums import AdapterType
        for processor_adapter in ProcessorAdapter.get_adapters(adapter_type=AdapterType.processors):
            processor_view = await processor_adapter.get_view()
            if processor_view.title.lower() == title.lower():
                return processor_adapter
        raise HTTPException(status_code=404, detail=f'Processor not found: {title} ')

    @staticmethod
    async def exchange_deserialization(exchange: dict):
        body_str = exchange.get("body", {}).get("stringBody", "{}")
        body_type = exchange.get('body', {}).get('type', 'string')

        # Получам контекст если нет то создаем
        context = exchange.get('context')
        context_str = context.get('stringBody') if context else '{}'
        try:
            input_context = orjson.loads(context_str)
        except ValueError:
            input_context = context_str

        # Получам входящие input headers если нет то создаем
        input_headers = exchange.get('inputHeaders', {})

        # Получам входящие headers если нет то создаем
        headers = exchange.get('headers', {})

        # Получсем тело сообщения
        input_body_str = exchange["inputBody"]["stringBody"]
        try:
            input_body = orjson.loads(input_body_str)
        except ValueError:
            input_body = body_str

        # Получаем параметры формы
        params = exchange.get("processor", {}).get("params", {})

        return dict(
            inputBody=input_body,
            inputHeaders=input_headers,
            headers=headers,
            context=input_context,
            context_exists=True if context else False,
            input_body_type=body_type,
            params=params
        )

    @staticmethod
    async def exchange_serialization(
            exchange: dict,
            context_exists: bool,
            body: dict | str,
            context: dict,
            input_headers: dict,
            headers: dict,
    ) -> dict:
        new_body = body
        exchange["inputHeaders"] = input_headers
        exchange["headers"] = headers
        # Сериализация в исходный формат JSON/String
        try:
            new_body_json = orjson.dumps(new_body).decode(encoding="utf-8")
            if isinstance(new_body, dict | list):
                new_body = new_body_json
                body_type = "json"
            else:
                raise Exception
        except Exception:
            try:
                xmltodict.parse(new_body)
                body_type = "xml"
            except Exception:
                body_type = "string"
        exchange["body"]["type"] = body_type
        exchange["body"]["stringBody"] = new_body if body_type == "json" else str(new_body)
        if not context_exists:
            return exchange

        new_context = context
        try:
            context_data_json = orjson.dumps(new_context).decode(encoding="utf-8")
            if isinstance(new_context, dict | list):
                context_data = context_data_json
                context_type = "json"
            else:
                raise Exception
        except Exception:
            context_type = "string"
            context_data = str(new_context)
        exchange["context"] = {
            "type": context_type,
            "stringBody": context_data,
            "outputBody": context_data,
        }
        return exchange
