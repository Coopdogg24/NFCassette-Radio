from flask import Flask, render_template, request, redirect
from Hardware import RFID 
from  Software import Spotify

app = Flask(__name__)
RFScanner = RFID()
Spotify = Spotify()

@app.route("/", methods = ['POST', 'GET'])
def index():
    try:
        currentlyPlaying = "Currently Playing: " + Spotify.getCurrentlyPlaying()["item"]["name"]
    except:
        currentlyPlaying = "Currently Playing: Nothing"

    if "spotifyURL" in request.form:
        if "album" in request.form["spotifyURL"]:
            writeData = "album:" + request.form["spotifyURL"][31:].split("?si=")[0]
        elif "track" in request.form["spotifyURL"]:
            writeData = "track:" + request.form["spotifyURL"][31:].split("?si=")[0]
        elif "playlist" in request.form["spotifyURL"]:
            writeData = "playl:" + request.form["spotifyURL"][34:].split("?si=")[0]
        return render_template('index.html',formatted_writeData = "Write Me: " + writeData, currently_playing=currentlyPlaying)
    
    elif "playbackControls" in request.form:
        if request.form["playbackControls"] == "play":
            Spotify.resume()
        elif request.form["playbackControls"] == "pause":
            Spotify.pause()
        elif request.form["playbackControls"] == "next":
            Spotify.next()
        elif request.form["playbackControls"] == "previous":
            Spotify.previous()
        return render_template('index.html', currently_playing=currentlyPlaying)
    
    elif "deviceControl" in request.form:
        if request.form["deviceControl"] == "listDevices":
            return render_template('index.html', device_list=Spotify.getDevices(), currently_playing=currentlyPlaying)

    return render_template("index.html", currently_playing=currentlyPlaying)

@app.route("/nfcRead/", methods = ['POST'])
def nfcRead():
    if request.form["NFCControl"] == "read":
        currentCard = ""
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

    else:
        if "album" in request.form["NFCControl"]:
            writeData = "album:" + request.form["NFCControl"][31:].split("?si=")[0]
        elif "track" in request.form["NFCControl"]:
            writeData = "track:" + request.form["NFCControl"][31:].split("?si=")[0]
        elif "playlist" in request.form["NFCControl"]:
            writeData = "playl:" + request.form["NFCControl"][34:].split("?si=")[0]
        RFScanner.Write(writeData)
    return render_template('index.html', currently_playing="Currently Playing: " + Spotify.getCurrentlyPlaying()["item"]["name"])

app.run(host='localhost', port=5000)