from pydantic import BaseModel


class ProcessedComponents(BaseModel):
    body: dict | str
    input_headers: dict
    headers: dict
    context: dict | str | None = None
    params: dict | None = None
