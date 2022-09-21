from pydantic import BaseModel
from typing import List

class JokeContractResponse(BaseModel):
    text:str
    
class JokeContractResponseList(BaseModel):
    jokes: List[JokeContractResponse] = []   