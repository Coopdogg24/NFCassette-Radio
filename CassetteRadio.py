import creds
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import json

### Spotify Setup ###
scope = ["user-modify-playback-state", "user-read-playback-state", "user-read-currently-playing", "app-remote-control, streaming"]
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=creds.client_ID, client_secret=creds.client_SECRET, redirect_uri=creds.redirect_url, scope=scope))

### RFID Setup ###
reader = SimpleMFRC522()
currentCard = ""

while True:
    print()
    print("Place card to read")
    play_uri = [str.strip("spotify:"+reader.read()[1])]
    
    if currentCard==reader.read()[0]:
        repeatedScan = False
    else:
        repeatedScan = True
        currentCard=reader.read()[0]

    if play_uri[0].startswith("spotify:track") and repeatedScan:
        sp.start_playback(device_id=creds.device_id, context_uri=None, uris=play_uri, offset=None, position_ms=None)
    elif play_uri[0].startswith("spotify:album") and repeatedScan:
        album_details = sp.album(play_uri[0].split(":")[2])
        track_uris=[]
        for i in album_details["tracks"]["items"]:
            track_uris.append(i["uri"])
        sp.start_playback(device_id=creds.device_id, context_uri=None, uris=track_uris, offset=None, position_ms=None)
