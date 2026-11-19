
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.tools import tool
from rich import print

# 1. Create a tool
@tool
def get_text_length(text: str) -> int:
    """Returns the number of characters in a given text."""
    return len(text)

# 2. Initialize model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=1
)

# 3. Bind tool
llm_with_tool = llm.bind_tools([get_text_length])

# 4. Normal LLM response
result1 = llm.invoke("hello")

# 5. LLM response with tool binding
result2 = llm_with_tool.invoke(
    "What is the length of the word hello?"
)

print("Normal response:")
print(result1)

print("\nResponse with tool binding:")
print(result2)