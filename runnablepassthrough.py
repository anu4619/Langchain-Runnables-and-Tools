from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableLambda,RunnablePassthrough
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
model =ChatOpenAI(model = "gpt-6-luna",temperature=1)
parser= StrOutputParser()

code_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a code generator"),
    ("human", "{topic}")
])

explain_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant who explains code in simple terms"),
    ("human", "explain the following code in  simple words:\n{code}")
])

#seq = code_prompt | model | parser | explain_prompt | model | parser

#result = seq.invoke({"topic":"write a code fro palindrome in python"})

#print (result)

seq = code_prompt | model | parser

seq2 = RunnableParallel(
    {"code_": RunnablePassthrough(),
     "explaination" : explain_prompt | model | parser}
)

chain = seq | seq2

result = chain.invoke({"topic" : "please write a code of palindrome in python"})

print(result['code_'])
print (result['explaination'])