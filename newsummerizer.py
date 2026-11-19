from dotenv import load_dotenv
load_dotenv()

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

search_tool = TavilySearchResults(max_results= 5)

llm = ChatOpenAI(model="gpt-6-luna", temperature=1)

prompt = ChatPromptTemplate.from_template(
    """
you are a helpful assistant
summerize the following news into clear bullet points
{news}"""
)



news_result = search_tool.run("Latest AI news of 2026")

chain = prompt|llm|StrOutputParser()

result = chain.invoke({"news":news_result})

print(result)