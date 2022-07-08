class Spotify:
    def __init__(self):
        import spotipy
        import creds
        import json
        from spotipy.oauth2 import SpotifyOAuth
        
        self.scope = ["user-modify-playback-state", "user-read-playback-state", "user-read-currently-playing", "app-remote-control, streaming"]
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=creds.client_ID, client_secret=creds.client_SECRET, redirect_uri=creds.redirect_url, scope=self.scope))
        self.deviceID = creds.device_id

    def playTrack(self, trackURI):
        """Description:
            Starts playing the parsed Track URI on the dedicated Spotify device 

        Args:
            trackURI (array): A single spotify URI for a specific track
        
        Example:
            ```playTrack(["3BIf974vl0lIEo3EY1XvD1"])```
        """
        self.sp.start_playback(device_id=self.deviceID, context_uri=None, uris=trackURI, offset=None, position_ms=None)
        return()

    def playAlbum(self, albumURI):
        """Description:
            Queues up all the songs in a playlist and plays it on the dedicated Spotify device

        Args:
            albumURI (string): A spotify URI for an entire album
        
        Example:
            ```playAlbum("1U0A6RPNJB05PtuBcaTM7o")```
        """
        album_details = self.sp.album(albumURI)
        track_uris=[]
        
        for i in album_details["tracks"]["items"]:
            track_uris.append(i["uri"])
        
        self.sp.start_playback(device_id=self.deviceID, context_uri=None, uris=track_uris, offset=None, position_ms=None)
        return()