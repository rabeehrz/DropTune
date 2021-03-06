from tinytag import TinyTag, TinyTagException
from base64 import b64encode
import os
metadata = {
    "title":"Untitled Track",
    "artist":"Unnamed Artist",
    "album":"Untitled Album"
}
def TagExtract(song):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    if song == None:
        with open('./static/dropplayer/images/albumartdefault.jpg', 'rb') as f:
            trackbin = f.read()
            track_img = str(b64encode(trackbin))[2:-3]
    else:
        track = TinyTag.get(song, image=True)
        track_img = track.get_image()
        title = track.title
        artist = track.artist
        album = track.album
        if title != None:
            metadata["title"] = title
        if artist != None:
            metadata["artist"] = artist
        if album != None:
            metadata["album"] = album
       
        track_img = str(b64encode(track_img))[2:-3]
    return metadata, track_img