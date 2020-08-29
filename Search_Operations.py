import requests
from Operations import Opertation
import json
class Search_Ops(Opertation):

    def __init__(self):
        super().__init__()
        self.payload = {}
        self.headers = super().getheaders() 
    
    
    def search_by_artist(self, item , type = "artist") -> json:
     
        url = f"https://api.spotify.com/v1/search?q={item}&type={type}"
        
        try:
            response = requests.request("GET", url, headers= self.headers, data = self.payload)
            return response.json()
        except:
           print("error")
        


