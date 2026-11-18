from urllib import response

from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
# 1. Prompt Template
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words"
)

# 2. Model
model = ChatOpenAI(model = "gpt-6-luna", temperature=1)

# 3. Output parser
parser = StrOutputParser()

# step by step manual flow

# format the prompt
#formatted_promppt = prompt.format_messages(topic = "Machine Learning")

#call the model manually
#response = model.invoke(formatted_promppt)

#parse the output manually
#final_output = parser.parse(response.content)

#print(final_output)

#two different prompts
short_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in 1-2 lines"
)

detailed_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in detail"
)

#input
topic = "Machine Learning"

chain = RunnableParallel({
    "short" : short_prompt | model | parser,
    "detailed" :detailed_prompt | model | parser

})

result = chain.invoke(topic)

print(result)

print(result['short'])
print(result['detailed'])