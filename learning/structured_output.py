from typing import Optional
from pydantic import BaseModel, Field
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI


LLM = "qwen3:8b"
# LLM = "llama3.1"

model = ChatOllama(
    model=LLM,
    temperature=0,
)

# model = ChatOpenAI(
#     model="gpt-4o-mini",
#     temperature=0,
# )


class Joke(BaseModel):
    """Joke to tell user."""

    setup: str = Field(description="The setup of the joke")
    punchline: str = Field(description="The punchline to the joke")
    rating: Optional[int] = Field(
        default=None, description="How funny the joke is, from 1 to 10"
    )


structured_llm = model.with_structured_output(Joke)

response = structured_llm.invoke("Tell me a joke about cats")

print(f"{response=}")
