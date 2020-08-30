import requests
from Operations import Opertation
import json
from Errors import ExpiredToken
class Search_Ops(Opertation):

    def __init__(self):
        super().__init__()
        self.payload = {}

    
    
    def search_by_artist(self, item , type = "artist") -> json:
     
        url = f"https://api.spotify.com/v1/search?q={item}&type={type}"
        
       
        response = requests.request("GET", url, headers= super().getHeaders() , data = self.payload)

        try:
            if(response.json()["error"]["status"] == 401):
                raise ExpiredToken
        except ExpiredToken as error:
            print(error) #TODO LOGGER

        return response.json()
        


