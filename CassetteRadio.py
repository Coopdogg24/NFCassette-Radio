from Hardware import RFID 
from  Software import Spotify
import asyncio

RFScanner = RFID()
Spotify = Spotify()

currentCard = ""

while True:
    scannedCard = RFScanner.Read()
    spotifyURI = [str.strip("spotify:"+scannedCard[1])]
    
    if currentCard==scannedCard[0]:
        repeatedScan = False
    else:
        repeatedScan = True
        currentCard=scannedCard[0]

    if spotifyURI[0].startswith("spotify:track") and repeatedScan:
        Spotify.playTrack(spotifyURI)
    elif spotifyURI[0].startswith("spotify:album") and repeatedScan:
        Spotify.playAlbum(spotifyURI[0].split(":")[2])
    elif spotifyURI[0].startswith("spotify:playl") and repeatedScan:
        Spotify.playPlaylist(spotifyURI[0].split(":")[2])