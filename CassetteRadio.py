import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

import creds
import RFID

### Spotify Setup ###
scope = ["user-modify-playback-state", "user-read-playback-state", "user-read-currently-playing", "app-remote-control, streaming"]
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=creds.client_ID, client_secret=creds.client_SECRET, redirect_uri=creds.redirect_url, scope=scope))

currentCard = ""

while True:
    print()
    print("Place card to read")
    
    scannedCard = RFID.Read()
    play_uri = [str.strip("spotify:"+scannedCard[1])]
    

    if currentCard==scannedCard[0]:
        repeatedScan = False
    else:
        repeatedScan = True
        currentCard=scannedCard[0]

    if play_uri[0].startswith("spotify:track") and repeatedScan:
        sp.start_playback(device_id=creds.device_id, context_uri=None, uris=play_uri, offset=None, position_ms=None)
    elif play_uri[0].startswith("spotify:album") and repeatedScan:
        album_details = sp.album(play_uri[0].split(":")[2])
        track_uris=[]
        for i in album_details["tracks"]["items"]:
            track_uris.append(i["uri"])
        sp.start_playback(device_id=creds.device_id, context_uri=None, uris=track_uris, offset=None, position_ms=None)
