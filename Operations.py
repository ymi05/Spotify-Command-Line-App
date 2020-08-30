
from tokenRetriever import getToken
class Opertation():



    def __init__(self):
        self.payload = {}

    def getHeaders(self) -> str:
        return {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': getToken()
        }



