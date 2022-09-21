from connectors import ChuckNorrisConnector
from fastapi import HTTPException
from contracts import JokeContractResponse
from contracts import JokeContractResponseList

class JokeController:
    def __init__(self) -> None:
        self.chuck_connector = ChuckNorrisConnector()
        
    async def get_random_joke(self) -> JokeContractResponse:
        
        random_joke_data = self.chuck_connector.get_random_joke().json()
        joke_contract_response = JokeContractResponse(
            text=random_joke_data['value']
        )
        return joke_contract_response

    async def get_random_joke_by_category(self, category:str) -> JokeContractResponse:
        
        random_joke_response = self.chuck_connector.get_random_joke_by_category(category)
        if random_joke_response.status_code == 404:
            raise HTTPException(status_code=404, detail=f"Joke not found with category: {category}")
        
        joke_contract_response = JokeContractResponse(
            text=random_joke_response.json()['value']
        )
        return joke_contract_response
        
    async def get_random_joke_by_filter(self, query:str, limit:int) -> JokeContractResponseList:
        
        random_joke_response = self.chuck_connector.get_random_joke_by_filter(query)
        if random_joke_response.status_code == 404 or random_joke_response.json()['total'] == 0:
            raise HTTPException(status_code=404, detail=f"Joke not found with query: {query}")
        
        joke_contract_response_list = JokeContractResponseList()
        
        for joke in random_joke_response.json()['result'][:limit]:
            joke_contract_reponse = JokeContractResponse(
                text=joke['value']
            )
            joke_contract_response_list.jokes.append(joke_contract_reponse)
            
        return joke_contract_response_list