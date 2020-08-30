from Search_Operations import Search_Ops
import json
import pyfiglet
from Items import Artist

from pyfiglet import figlet_format
print(figlet_format('Spotify!', font='starwars'))



item = str(input("Please enter an artist's name:\t"))


results = Search_Ops().search_by_artist(item)

        

artist_dict = {}
counter = 1
for result in results["artists"]["items"]:
    artist_dict[counter] = Artist(result)
    print(f"{counter}. {artist_dict[counter].name}")
    counter += 1


