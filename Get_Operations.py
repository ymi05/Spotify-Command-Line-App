import requests
from Operations import Opertation
import json
from Errors import ExpiredToken
class Get_Ops(Opertation):


    def __init__(self):
        super().__init__()
        self.payload = {}
   
    
    
    def getAlbum_by_artist(self, artist_id , type = "artist") -> json:
     
        url = f"https://api.spotify.com/v1/artists/{artist_id}/albums"
        
        response = requests.request("GET", url, headers= super().getHeaders() , data = self.payload)

        try:
            if(response.json()["error"]["status"] == 401):
                raise ExpiredToken
        except ExpiredToken as error:
            print(error) #TODO LOGGER
 
            
        finally:
            return response.json()

    def getSongs_by_album(self , album_id):
        url = f"https://api.spotify.com/v1/albums/{album_id}"
        
        response = requests.request("GET", url, headers= super().getHeaders() , data = self.payload)

        try:
            if(response.json()["error"]["status"] == 401):
                raise ExpiredToken
        except ExpiredToken as error:
            print(error) #TODO LOGGER
 
            
        finally:
            return response.json()


operationsObj = Get_Ops()