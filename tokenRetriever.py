import requests

from secrets import CLIENT_ID , CLIENT_SECRET

def getToken():
    
    grant_type = 'client_credentials'
    body_params = {'grant_type' : grant_type}

    url='https://accounts.spotify.com/api/token'
    response = requests.post(url, data=body_params, auth = (CLIENT_ID, CLIENT_SECRET)) 
    return f"{response.json()['token_type']} {response.json()['access_token']}"


