## ouput parsers for response Formatting 


from langchain_core.prompts import PromptTemplate
from langchain.output_parsers.json import SimpleJsonOutputParser 

json_prompt=PromptTemplate.from_template(
    "Return  a JSON object with a `answer` key that answers the following question.{question}"
)


json_parser = SimpleJsonOutputParser()

json_chain= json_prompt | llmModel | json_parser

## see result :
# here json_chain output will result in dict type..

# Furthermore,

# Optionally,we can use Pydantic Model to define  a custom output format 
# we can do it as follows:

from langchain_core.prompts import PromptTemplate
from langchain.output_parsers.json import JsonOutputParser 
from langchain_core.pydantic_v1 import BaseModel,Field 





# define a Pydantic Object with the desired ouput format.

class Joke(BaseModel):
    setup : str = Field(description='question to set up a joke')
    punchline : str = Field(description='answer to resolve the joke')



parser=JsonOutputParser(pydantic_object=Joke)  # defining parser reffering the Pydantic Object. 


# defining base models help in defining our outputs as we expected,so explore it..




