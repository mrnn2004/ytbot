from ytmusicapi import YTMusic
import json
from pytube import YouTube


ytmusic = YTMusic('headers_auth.json')
playlistId = ytmusic.create_playlist('test', 'test description')
search_results = ytmusic.search('7rings')

aList = search_results
jsonStr = json.dumps(aList)
print(jsonStr)



ytmusic.add_playlist_items(playlistId, [search_results[1]['videoId']])

print('-------------------------------------------------------------------------------------------------------')

yt = YouTube('https://music.youtube.com/watch?v=XZ868t23Pb4')

print(yt.streams)
