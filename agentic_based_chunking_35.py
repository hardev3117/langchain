from pydantic import BaseModel, Field
from langchain.chat_models import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

class Person(BaseModel):
    name: str = Field(description="The person's name")
    age: int = Field(description="The person's age")

llm = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0)
structured_llm = llm.with_structured_output(Person)

result = structured_llm.invoke("Alice is 30 years old.")
print(result)  # Returns a Person instance with name and age
