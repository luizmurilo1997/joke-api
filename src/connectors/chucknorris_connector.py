import requests
from requests import Response


class ChuckNorrisConnector:
    
    def get_random_joke(self) -> Response:
        response = requests.get('https://api.chucknorris.io/jokes/random')
        return response
        
    def get_random_joke_by_category(self, category:str) -> Response:
        response = requests.get(f'https://api.chucknorris.io/jokes/random?category={category}')
        return response
    
    def get_random_joke_by_filter(self, query:str) -> Response:
        response = requests.get(f'https://api.chucknorris.io/jokes/search?query={query}')
        return response
    
    