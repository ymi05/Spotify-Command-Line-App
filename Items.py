import requests
from Get_Operations import operationsObj
import webbrowser 

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
        results = operationsObj.getAlbum_by_artist(self.__artist_Id)
        counter = 1
        for result in results["artists"]["items"]:
            self.__artist_Albums[counter] = Album(result)
            counter += 1


    

        



class Album():
    def __init__(self , data):
        self.__album_ID = data["uri"].split("spotify:album:")[1]
        self.__album_Name = data["name"]
        self.__album_releaseDate = data["release_date"]
        self.__album_totalTracks = data["total_tracks"]
        self.__album_URL = data["external_urls"]["spotify"]
        self.__album_Songs = {}


    @property
    def ID(self):
        return self.__album_ID
    
    @property
    def name(self):
        return self.__album_Name
    
    @property
    def releaseDate(self):
        return self.__album_releaseDate

    
    @property 
    def totalTracks(self):
        return self.__album_totalTracks

    @property 
    def URL(self):
        return self.__album_URL

    def load_songs(self):
        results = operationsObj.getSongs_by_album(self.__album_ID)
        counter = 1
        for result in results["items"]:
            self.__album_Songs[counter] = Song(result)
            counter += 1
        



class Song():
    def __init__(self , data):
        self.__song_ID = data["id"]
        self.__song_Name = data["name"]
        self.__song_Duration = data["duration_ms"]/3600
        self.__isExplicit = True if data["explicit"] == "true" else False
        self.__song_URL = data["external_urls"]["spotify"]



    @property
    def ID(self):
        return self.__song_ID

    @property
    def name(self):
        return self.__song_Name

    @property
    def duration(self):
        return self.__song_Duration

    @property
    def isExplicit(self):
        return self.__isExplicit

    def playSong_InBrowser(self):
        webbrowser.open_new(self.__song_URL)


