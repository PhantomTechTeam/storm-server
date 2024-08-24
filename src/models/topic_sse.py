from pydantic import BaseModel, Field


class TopicInputSSE(BaseModel):
    topic: str
    query_params: dict = Field(
        default={"ai_model": "gpt-3.5", "retriever_model": "duckduckgo", "user_id": ""}
    )
