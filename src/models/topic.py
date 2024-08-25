from pydantic import BaseModel, Field


class TopicInput(BaseModel):
    topic: str
    query_params: dict = Field(
        default={"ai_model": "gpt-3.5", "retriever_model": "duckduckgo"}
    )
