import os
import sys
import spotipy
import spotipy.util as util

if 'SPOTIFY_USERNAME' not in os.environ:
    print(
        '''
        Set your Spotify username on the command line like so:

        export SPOTIFY_USERNAME='your_username'
        ''')
    sys.exit()

USERNAME = os.environ['SPOTIFY_USERNAME']

def scope_token(scope):
    token = util.prompt_for_user_token(USERNAME, scope)
    return spotipy.Spotify(token)

def spot_help():
    print(
        '''
        List of commands:

        spot help                    - lists all commands and what they do
        spot play                    - plays from where you left off
        spot play [song_name]        - plays first result from search for song_name
        spot play pl [playlist_name] - plays first result from search for playlist_name
        spot play al [album_name]    - plays first result from search for album_name
        spot play ar [artist_name]   - plays first result from search for artist_name
        spot pause                   - pauses current song
        spot save                    - save current song to library (if unsaved)
        spot n	                     - plays next song in queue
        spot p	                     - plays previous song in queue
        spot re	                     - plays replay current song
        ''')

def play(keywords):
    # Handles all spot play commands
    if not keywords:
        resume()
    # if keywords[1] == 'pl':
    #     play_pl(keywords[2:])

def resume():
    # Implements 'spot play'.
    sp = scope_token('user-modify-playback-state')
    try:
        sp.start_playback()
    except spotipy.client.SpotifyException as e:
        print(str(e))

def pause():
    # Implements 'spot pause'.
    sp = scope_token('user-modify-playback-state')
    try:
        sp.pause_playback()
    except spotipy.client.SpotifyException as e:
        print(str(e))

def spot_next():
    # Implements 'spot n'.
    sp = scope_token('user-modify-playback-state')
    try:
        sp.next_track()
    except spotipy.client.SpotifyException as e:
        print(str(e))

def spot_prev():
    # Implements 'spot n'.
    sp = scope_token('user-modify-playback-state')
    try:
        sp.previous_track()
    except spotipy.client.SpotifyException as e:
        print(str(e))

# scope = 'user-library-read'
#
# if len(sys.argv) > 1:
#     username = sys.argv[1]
# else:
#     print("Usage: %s username" % (sys.argv[0],))
#     sys.exit()
#
# token = util.prompt_for_user_token(USERNAME, scope)
#
# if token:
#     sp = spotipy.Spotify(auth=token)
#     results = sp.current_user_saved_tracks()
#     for item in results['items']:
#         track = item['track']
#         print(track['name'] + ' - ' + track['artists'][0]['name'])
#     results = sp.search(q='Young Thug', type='artist')
#     for item in results['artists']['items']:
#         print(item['name'])
# else:
#     print("Can't get token for", USERNAME)
