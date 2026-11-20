from unittest import result

from dotenv import load_dotenv
load_dotenv()
from rich import print
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage
# 1. Create a tool
@tool
def get_text_length(text: str) -> int:
    """Returns the number of characters in a given text."""
    return len(text)
tools={
    "get_text_length" : get_text_length
}
# 2. Initialize model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=1
)

# 3. Bind tool
llm_with_tool = llm.bind_tools([get_text_length])

messages= []
prompt=input("You:")
query = HumanMessage(prompt)
messages.append(query)

result = llm_with_tool.invoke(messages)

messages.append(result)



if result.tool_calls:
    tool_name = result.tool_calls[0]['name']
    tool_message = tools[tool_name].invoke(result.tool_calls[0])
    messages.append(tool_message)
    

result = llm_with_tool.invoke(messages)
print(result.content)