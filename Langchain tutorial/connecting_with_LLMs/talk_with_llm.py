import os 
from dotenv import load_dotenv,find_dotenv

_ = load_dotenv(find_dotenv())

# open_ai_key= os.environ["OPEN_AI_KEY"]


# Completion model 

# from langchain_openai import OpenAI

# llmModel=OpenAI()


# response= llmModel.invoke("Tell me one fact about country Nepal") # this will get one shot output.


# # for streaming output from LLM,perform this operation.
# for chunk in llmModel.stream(
#     "tell me one fact about country Nepal"
# ):
#     print(chunk,end="",flush =True)


# ## if we want to vary behaviour of our LLM,

# creativeLLMModel =OpenAI(temperature=0.9)  # Temperature: more or less creativity.

# response1 = creativeLLMModel.invoke("Tell me one fact about country Nepal") 

# print(response1)


# #### CHAT MODELS:
# # for this models,you can give system prompt as well as user prompt.

# from langchain_openai import ChatOpenAI

# chatModel=ChatOpenAI(model="gpt-3.5-turbo-0125")

# messages =[ 
#     ("system","You are an historian expert in the Kennedy family."),
#     ("human","Tell me one curious thing about JFK.")    
# ]
# response2=chatModel.invoke(messages)

# print(response) # langchain chatopen ai response answers as AI message  and message we give will be human message.

# # as it response with ai message so 
# print(response.content)

# # also explore
# print(response.response_metadata)

# response.schema()


# # But previous versions,we used to pass like this:

# from langchain_core.messages import HumanMessage,SystemMessage
# from langchain_core.prompts import ChatPromptTemplate 

# messages = [
#     SystemMessage(content=""),
#     HumanMesage(content=""),

# ]
# response = chatModel.invoke(messages)




### ALTERNATIVE LLM '

open_ai_key= os.environ["GROQ_API_KEY"]

from langchain_groq import ChatGroq

llamaChatModel = ChatGroq(
    model="llama-3.1-8b-instant"
)

messages =[ 
    ("system","You are an historian expert in the Kennedy family."),
    ("human","Tell me one curious thing about JFK.")    
]

response5 = llamaChatModel.invoke(messages)
print(response5.content)
print(response5.response_metadata)


