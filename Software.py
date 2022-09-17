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
    
    def playPlaylist(self, playlistURI):
        """Description:
            Queues up all the songs in a playlist and plays it on the dedicated Spotify device

        Args:
            playlistURI (string): A spotify URI for an entire playlist
        
        Example:
            ```playPlaylist("37i9dQZF1DXcBWIGoYBM5M")```
        """
        playlist_details = self.sp.playlist(playlistURI)
        track_uris=[]
        
        for i in playlist_details["tracks"]["items"]:
            track_uris.append(i["track"]["uri"])
        
        self.sp.start_playback(device_id=self.deviceID, context_uri=None, uris=track_uris, offset=None, position_ms=None)
        return()

    def pause(self):
        """Description:
            Pauses the current song on the dedicated Spotify device

        Args:
            n/a
        """
        self.sp.pause_playback(device_id=self.deviceID)
        return()

    def resume(self):
        """Description:
            Resumes the current song on the dedicated Spotify device

        Args:
            n/a
        """
        self.sp.start_playback(device_id=self.deviceID)
        return()

    def next(self):
        """Description:
            Skips to the next song on the dedicated Spotify device

        Args:
            n/a
        """
        self.sp.next_track(device_id=self.deviceID)
        return()

    def previous(self):
        """Description:
            Skips to the previous song on the dedicated Spotify device

        Args:
            n/a
        """
        self.sp.previous_track(device_id=self.deviceID)
        return()

    def volume(self, volume):
        """Description:
            Sets the volume of the dedicated Spotify device

        Args:
            volume (int): A number between 0 and 100
        """
        self.sp.volume(volume, device_id=self.deviceID)
        return()

    def shuffle(self, shuffle):
        """Description:
            Sets the shuffle state of the dedicated Spotify device

        Args:
            shuffle (bool): True or False
        """
        self.sp.shuffle(shuffle, device_id=self.deviceID)
        return()

    def repeat(self, repeat):
        """Description:
            Sets the repeat state of the dedicated Spotify device

        Args:
            repeat (string): "track", "context", or "off"
        """
        self.sp.repeat(repeat, device_id=self.deviceID)
        return()

    def getCurrentlyPlaying(self):
        """Description:
            Gets the currently playing song on the dedicated Spotify device

        Args:
            n/a
        """
        return(self.sp.currently_playing())

    def getDevices(self):
        """Description:
            Gets the devices that are currently connected to the Spotify account

        Args:
            n/a
        """
        return(self.sp.devices())

    def getPlaylists(self):
        """Description:
            Gets the playlists that are currently connected to the Spotify account

        Args:
            n/a
        """
        return(self.sp.current_user_playlists())

    def getArtist(self, artistURI):
        """Description:
            Gets the artist details

        Args:
            artistURI (string): A spotify URI for an artist
        """
        return(self.sp.artist(artistURI))

    def getArtistAlbums(self, artistURI):
        """Description:
            Gets the albums by an artist

        Args:
            artistURI (string): A spotify URI for an artist
        """
        return(self.sp.artist_albums(artistURI))

    def getArtistTopTracks(self, artistURI):
        """Description:
            Gets the top tracks by an artist

        Args:
            artistURI (string): A spotify URI for an artist
        """
        return(self.sp.artist_top_tracks(artistURI))

    def getArtistRelatedArtists(self, artistURI):
        """Description:
            Gets the related artists by an artist

        Args:
            artistURI (string): A spotify URI for an artist
        """
        return(self.sp.artist_related_artists(artistURI))

