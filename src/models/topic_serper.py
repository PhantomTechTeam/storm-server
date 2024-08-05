from pydantic import BaseModel


class SerperInput(BaseModel):
    topic: str
    query_params: dict[str, str]
