from pydantic import BaseModel, Field


class SerperInput(BaseModel):
    topic: str
    query_params: dict = Field(default={"autocorrect": True, "num": 10, "page": 1})
    ai_model: str = Field(
        examples=["gpt-3.5", "gpt-4-o", "mixed-openai", "claude"], default="gpt-4-o"
    )
