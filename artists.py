import requests
from Get_Operations import Get_Ops
class Artist:
    def __init__(self , data):
 
        '''using the json data from before we can intitalize an object from each result rather than using
        the ID of each artist and and requesting the SAME data again but for one artist'''
        self.__artist_Id = data["id"]
        self.__artist_Name = data["name"]
        self.__artist_Popularity = data["popularity"]
        self.__artist_Followers = data["followers"]["total"]
        self.__artist_SpotifyProfile = data["external_urls"]["spotify"]
        self.__artist_images = None #!TODO
        self.__artist_Albums = {}


    @property
    def id(self):
        return self.__artist_Id
    @property
    def name(self):
        return self.__artist_Name
    @property
    def popularity(self):
        return self.__artist_Popularity
    @property
    def followers(self):
        return self.__artist_Followers
    @property
    def profile(self):
        return self.__artist_SpotifyProfile

    def load_albums(self):
        results = Get_Ops().getAlbum_by_artist(self.__artist_Id)
        counter = 1
        for result in results["artists"]["items"]:
            self.__artist_Albums[counter] = Album(result)
            counter += 1


    

        



class Album():
    def __init__(self , data):
        self.__album_Name = data["name"]
        self.__album_ReleaseDate = data["release_date"]
        self.__album_Tracks = data["total_tracks"]
        self.__album_URL = data["external_urls"]["spotify"]
        