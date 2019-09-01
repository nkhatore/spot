import os
import sys
import spotipy
import spotipy.util as util

if 'SPOTIFY_USERNAME' not in os.environ:
    print(
        '''
        Set your Spotify username in ~/.bash_profile like so:

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
        spot curr                    - prints info on current song
        spot pause                   - pauses current song
        spot save                    - save current song to library (if unsaved)
        spot n	                     - plays next song in queue
        spot p	                     - plays previous song in queue
        spot r 	                     - turns replay mode on/off on current track
        spot rc                      - turns replay mode on/off for context (album, playlist, etc.)
        spot s                       - turns shuffle mode on/off
        ''')

def play(keywords):
    # Handles all spot play commands
    if not keywords:
        resume()
    elif keywords[0] == 'pl':
        play_playlist(keywords[1:])
    elif keywords[0] == 'al':
        play_album(keywords[1:])
    elif keywords[0] == 'ar':
        play_artist(keywords[1:])
    else:
        play_track(keywords)

def resume():
    # Implements 'spot play'.
    sp = scope_token('user-modify-playback-state')
    try:
        sp.start_playback()
    except spotipy.client.SpotifyException as e:
        print(str(e))

def curr():
    # Implements 'spot curr'
    sp = scope_token('user-read-currently-playing')
    try:
        current = sp.current_user_playing_track()
        track = current['item']['name']
        artist = current['item']['artists'][0]['name']
        album = current['item']['album']['name']
        track_info = track + '    ' + ' ' * max(0, 5 - len(track)) + artist + '    ' + ' ' * max(0, 6 - len(artist)) + album
        print('\n' + '        Track' + ' ' * max(0, len(track) - 1) + 'Artist' + ' ' * max(4, len(artist) - 2) + 'Album')
        print('        ' + '-' * max(5, len(track)) + '    ' + '-' * max(6, len(artist)) + '    ' + '-' * max(5, len(album)))
        print('        ' + track_info + '\n')
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

def play_playlist(keywords):
    print('pl')

def play_album(keywords):
    print('al')

def play_artist(keywords):
    print('al')

def play_track(keywords):
    print(keywords)
    print('track')
    query = ' '.join(keywords)

def save():
    sp = scope_token('player-read-private')
    sp2 = scope_token('player-read-collaborative')
    try:
        sp2.user_playlists()
    except spotipy.client.SpotifyException as e:
        print(str(e))

def repeat(context=False):
    # Implements 'spot r' and 'spot rc'.
    sp = scope_token('user-modify-playback-state')
    try:
        playback_state = sp.current_playback()
        if playback_state['repeat_state'] == 'off':
            if context:
                sp.repeat('context')
            else:
                sp.repeat('track')
        else:
            sp.repeat('off')
    except spotipy.client.SpotifyException as e:
        print(str(e))

def shuffle():
    # Implements 'spot s'.
    sp = scope_token('user-modify-playback-state')
    try:
        playback_state = sp.current_playback()
        if playback_state['shuffle_state']:
            sp.shuffle(False)
        else:
            sp.shuffle(True)
    except spotipy.client.SpotifyException as e:
        print(str(e))

# def modify_playback(sp_func):
#     # Helper to
#     sp = scope_token('user-modify-playback-state')
#     try:
#         sp_func()
#     except spotipy.client.SpotifyException as e:
#         print(str(e))
