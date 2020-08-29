from Search_Operations import Search_Ops
import json

from artists import Artist


item = str(input("Please enter an artist's name:\t"))


results = Search_Ops().search_by_artist(item)

        

artist_dict = {}
counter = 1
for result in results["artists"]["items"]:
    artist_dict[counter] = Artist(result)
    print(f"{counter}. {artist_dict[counter].name}")
    counter += 1


