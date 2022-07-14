from ytmusicapi import YTMusic

ytmusic = YTMusic('headers_auth.json')
playlistId = ytmusic.create_playlist('test', 'test description')
search_results = ytmusic.search('7rings')
f = open('search_result.json', 'w')
f.write(str(search_results))
f.close
ytmusic.add_playlist_items(playlistId, [search_results[0]['videoId']])


