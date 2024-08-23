from pydantic import BaseModel, Field


class TopicInputSSE(BaseModel):
    topic: str
    ai_model: str = Field(
        examples=["gpt-3.5", "gpt-4-o", "mixed-openai", "claude"], default="gpt-4-o"
    )
    retriever_model: str = Field(
        examples=["you", "serper", "brave", "searxng", "duckduckgo"], default="duckduckgo"
    )
    user_id: str
