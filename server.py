from flask import Flask, json, jsonify, render_template, request, redirect, session
import logging
from spotify_keys import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
from flask_cors import CORS 
from collections import defaultdict
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials


logging.basicConfig(filename="log.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

log = logging.getLogger()
log.setLevel(logging.DEBUG)
app = Flask(__name__)
CORS(app)
app.secret_key = "\xcb\xa0\x030\xc2\xe4x\xbb\x9fw\xdc/"


greenday_uri = "spotify:artist:7oPftvlwr6VrsViSDV7fJY"
urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
usa_idiot = "spotify:track:6nTiIhLmQ3FWhvrGafw2zj"
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=CLIENT_ID,
                                                                         client_secret=CLIENT_SECRET))


# content = sp.artist_top_tracks(greenday_uri, country="US")
# response = sp.artist_top_tracks(urn)

# @app.route("/playlist", methods=['POST','GET'])
def playlist(playlist_name):
    # link = request.form['playlist']
    # https://open.spotify.com/playlist/54HWyh4h3DkHAyP4TcojxC?si=72f6ab8d6fb149fd        
    content = sp.playlist_items(playlist_name)
    # if time, create error page for entering private playlist (error 404)

    # initializes tracklist and gets all songs past 100 limit
    tracks = []
    tracks.extend(content['items'])
    while content['next']:
        content = sp.next(content)
        tracks.extend(content['items'])


    #gets rid of locally uploaded 
    for item in tracks:
        if item['is_local']:
            tracks.remove(item)

    tids = []
    for t in range(0, len(tracks)):
        tids.append(tracks[t]['track']['uri'])
    
    features = sp.audio_features(tids)

    log.debug("features", features)
    return features

# @app.route('/track', methods=['GET', 'POST'])
def track(track_name):
    track_id = sp.search(track_name,type='track')['tracks']['items'][0]['uri'] 
    features = sp.audio_features(track_id)
    session['data'] = (features)
    return features

# @app.route("/album", methods=['GET', 'POST'])
def album(album_name):
    album_id = sp.search(album_name,type='album')['albums']['items'][0]['uri'] 
    album = sp.album(album_id)
    tids = []
    for t in album['tracks']['items']:
        tids.append(t['uri'])
        
    features = sp.audio_features(tids)
    session['data'] = (features)
    return features

# @app.route("/viz")
def viz(data):
# pitch class notation for key: https://en.wikipedia.org/wiki/Pitch_class 
    features = defaultdict(list)
    size = len(data)
    feat_list = ['acousticness', 'danceability', 'energy', 'instrumentalness',
                'key', 'liveness', 'loudness', 'mode', 'speechiness', 'tempo',
                'time_signature', 'valence']
    for track in data:
        for f in feat_list:
            features[f].append(track[f])

    avg_features = {}
    for f in features:
        avg_features[f] = sum(features[f]) / size
    avg_features['key'] = int(avg_features['key'])
    avg_features['mode'] = int(avg_features['mode'])
    log.info("avg_features", avg_features)
    return avg_features


@app.route("/", methods=['POST'])
def form_to_features():
    data = request.json
    content = data['content']
    music_input = data['musicInput']
    log.debug("handling form in flask")

    #sp_info will be a spotify object, content should be a string
    if music_input == "track":
        sp_info = track(content)
    elif music_input == "album":
        sp_info = album(content)
    elif music_input == "playlist":
        sp_info = playlist(content)
    else:
        return Exception("Invalid music input type")
    
    return jsonify(viz(sp_info))


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)


