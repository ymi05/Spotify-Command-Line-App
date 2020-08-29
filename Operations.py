class Opertation():
    def __init__(self):
        #!IMPORTANT: FIND A WAY TO GET THE NEW TOKEN
        self.OAuth_Token = None
        self.payload = {}
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': self.OAuth_Token
        }


    def getheaders(self) -> str:
        return self.headers






    
            


