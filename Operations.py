class Opertation():
    def __init__(self):
        #!IMPORTANT: FIND A WAY TO GET THE NEW TOKEN
        self.OAuth_Token = "Bearer BQAkG7cUNVwHAvddoYUNHgsrrMxloni9-yQXFBOjAXitwUGE9t9wHKv2Fynat372n-kuHinAMqlgPHHiWWTBzma2btjMRTI-7YgzvMNCF-ohVYf5iNjw6HfQZPqLlU-3bto-ja8z3D9yH9sE-ye9o6OePEs3bRw"
        self.payload = {}
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': self.OAuth_Token
        }


    def getheaders(self) -> str:
        return self.headers






    
            


