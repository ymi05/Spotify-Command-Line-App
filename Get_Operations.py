import requests
from Operations import Opertation
import json

class Get_Ops(Opertation):

    def __init__(self):
        super().__init__()
        self.payload = {}
        self.headers = super().getheaders()
    
    
    def getAlbum_by_artist(self, artist_id , type = "artist") -> json:
     
        url = f"https://api.spotify.com/v1/artists/{artist_id}/albums"
        
        try:
            response = requests.request("GET", url, headers= self.headers, data = self.payload)
            return response.json()
        except:
           print("error")
        
