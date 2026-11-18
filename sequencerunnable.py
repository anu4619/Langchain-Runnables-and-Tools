from urllib import response

from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

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

chain = prompt | model | parser


result = chain.invoke({"topic": "Machine Learning"})

print(result)