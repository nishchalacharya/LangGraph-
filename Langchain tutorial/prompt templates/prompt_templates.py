
import os 
from dotenv import load_dotenv 

load_dotenv()

groq_api_key =os.environ["GROQ_API_KEY"]


from langchain_core.messages import HumanMessage,SystemMessage
from langchain_core.prompts import ChatPromptTemplate 
from langchain_groq import ChatGroq

llamaChatModel = ChatGroq(
    model="llama-3.1-8b-instant"
)

# messages = [
#     SystemMessage(content=""),
#     HumanMessage(content=""),

# ]
# response = llamaChatModel.invoke(messages)


## Prompts and Prompts Templates 
# for completions model 
from langchain_core.prompts import PromptTemplate


Prompt_template =PromptTemplate.from_template(
    "Tell me {adjective} story about {topic}"
)

llmModelPrompt =Prompt_template.format(
    adjective="curious",
    topic="Tesla"
)

res= llamaChatModel.invoke(llmModelPrompt)

print(res.content)


## for chat completion models 

chat_template=ChatPromptTemplate.from_messages(
    [
        ("system","You are an {profession} expert on {topic}."),
        ("human","Hello,Mr. {profession},can you please answer a question"),
        ("ai","Sure!"),
        ("human","{user_input}")
    ]
)


messages = chat_template.format_messages(
    profession="Historian",
    topic="The Kennedy family",
    user_input="How many grandchildren had Joseph P. Kennedy?"
)

response=llamaChatModel.invoke(messages)
print(response.content)


## above is example of few shot prompting 
# techniques of prompting:
# - zero-shot prompting
# - few shot prompting 
# - chain of thought prompting
# - multi step prompting 
# - chain of thought with few shot prompting 


## Let's try few shot prompting techniques .
 

from langchain_core.prompts import FewShotChatMessagePromptTemplate

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




#### Chains 

