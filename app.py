from flask import Flask, json, jsonify, render_template, request, redirect, session
import logging
import time
from collections import defaultdict
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials


log = logging.getLogger("logs")
app = Flask(__name__)
app.secret_key = "\xcb\xa0\x030\xc2\xe4x\xbb\x9fw\xdc/"


CLIENT_ID = "83641f1ffde843d3abeba575870d5817"
CLIENT_SECRET = "ffc7416953e04e499c0a956f339ada71"

greenday_uri = "spotify:artist:7oPftvlwr6VrsViSDV7fJY"
urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
usa_idiot = "spotify:track:6nTiIhLmQ3FWhvrGafw2zj"
# spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, 
#                                                     client_secret=CLIENT_SECRET,
#                                                     redirect_uri = "http://127.0.0.1:5000/",
#                                                     scope='user-library-read'))

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=CLIENT_ID,
                                                                         client_secret=CLIENT_SECRET))

log.info(sp)

content = sp.artist_top_tracks(greenday_uri, country="US")
# songs = content.items()
response = sp.artist_top_tracks(urn)

@app.route('/track', methods=['GET', 'POST'])
def song():
    if request.method == "GET":
        return  '''
                <form method = post>
                    <p><input type=text name=song>
                </form>
                '''
    else:
        search = request.form['song']
        track_id = sp.search(search,type='track')['tracks']['items'][0]['uri'] 
        features = sp.audio_features(track_id)
        session['data'] = (features)
        return redirect('/viz')

@app.route("/album", methods=['GET', 'POST'])
def album():
    if request.method == "GET":
        return  '''
                <form method = post>
                    <p><input type=text name=album>
                </form>
                '''
    else:
        search = request.form['album']
        album_id = sp.search(search,type='album')['albums']['items'][0]['uri'] 
        album = sp.album(album_id)
        tids = []
        for t in album['tracks']['items']:
            tids.append(t['uri'])
            
        features = sp.audio_features(tids)
        session['data'] = (features)
        return redirect('/viz')

@app.route("/viz")
def viz():
# pitch classs notation for key: https://en.wikipedia.org/wiki/Pitch_class 

    data = session.get('data', None)
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
    return avg_features
    



"""
 {"access_token":"
 BQDxMfdZkI-xDTaxCV59CqogMf6q8nTmaAmXGcyj1GpuRz8WJ4PSWY2Y8EKW6SX5bFmncIoFKi2b7GL0ULUJPaN3HHqeVZwyoSua9Xl-Y2B_Zc75u3U
 "token_type":"Bearer","expires_in":3600}
 
0XNa1vTidXlvJ2gHSsRi4A?si=-54XNiF0Su-PAXBxt9LQkw
 """