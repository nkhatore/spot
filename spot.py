import os
import sys
import spotipy
import spotipy.util as util

print(os.environ['SPOTIFY_USERNAME'])

if 'SPOTIFY_USERNAME' not in os.environ:
    print(
        '''
        Set your Spotify username on the command line like so:

        export SPOTIFY_USERNAME='your_username'
        ''')
    sys.exit()

USERNAME = os.environ['SPOTIFY_USERNAME']

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
