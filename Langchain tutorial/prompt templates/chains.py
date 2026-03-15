 
import os 
from dotenv import load_dotenv 
from langchain_core.prompts import FewShotChatMessagePromptTemplate
from langchain_core.prompts import ChatPromptTemplate 

from langchain_groq import ChatGroq



load_dotenv()

groq_api_key =os.environ["GROQ_API_KEY"]





llamaChatModel = ChatGroq(
    model="llama-3.1-8b-instant"
)

examples =[
    {"input":"hi!","output":"!hola "},
    {"input":"bye !","output":"adios"}  # spanish language 
]


example_prompt = ChatPromptTemplate.from_messages(
    [
        ("human","{input}"),
        ("ai","{output}")
    ]
)

few_shot_prompt=FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples
)

final_prompt =ChatPromptTemplate.from_messages(
    [

        ("system","You are an English-spanish translator."),
        few_shot_prompt,
        ("human","{input}"),
    ]
)


chain = final_prompt | llamaChatModel   # this is actually called langchain Expressions Language.

a= chain.invoke({"input":"How are you?"})
print(a.content)


