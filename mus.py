
import os
import requests
import shutil
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
from spotipy.oauth2 import SpotifyClientCredentials
#User id :  11156533090
# Get the username from terminal
username = sys.argv[1]
scope = 'user-read-private user-read-playback-state user-modify-playback-state'


# Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username, scope) # add scope
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope) # add scope

# Create our spotify object with permissions
spotifyObject = spotipy.Spotify(auth=token)

# # Get current device
devices = spotifyObject.devices()
deviceID = devices['devices'][0]['id']

# # Current track information
# track = spotifyObject.current_user_playing_track()
# artist = track['item']['artists'][0]['name']
# track = track['item']['name']

# if artist != "":
#     print("Currently playing " + artist + " - " + track)

# User information
user = spotifyObject.current_user()
displayName = user['display_name']
followers = user['followers']['total']

#lista das bandas 
#bands = ["spotify:artist:5njAynPPzwutQXEG894dUC","spotify:artist:3HQ7qP6FF9Qpgc8OCsDaBH","spotify:artist:6pTMMeBBPWFMl9Mm26IH1J","spotify:artist:2ye2Wgw4gimLv2eAKyk1NB","spotify:artist:22WZ7M8sxp5THdruNY3gXt","spotify:artist:7ltDVBr6mKbRvohxheJ9h1"]

bands = ["spotify:artist:2pkZFQGkxsNYlJK5jO4z3L","spotify:artist:0T6eNp8abRNgNpnN1LLFF5","spotify:artist:1d7OHfSeHLlpu0IOiakjI3","spotify:artist:3f3Cj4QJUOfmi0xNAMSeGt","spotify:artist:4e1AHxzzjlvf3Lh0xL4DIJ","spotify:artist:4M6ymZ0NfSGj2RQT7EfSiM","spotify:artist:6pTMMeBBPWFMl9Mm26IH1J","spotify:artist:5cWd0Lh2HuI7q8KPY4gZoU","spotify:artist:5eBGSUHWi91BoXwkusybrP","spotify:artist:77c4OV5H4v9UtyvyLTtn0y","spotify:artist:3fiacmVyfQUItNnU4ImgJf","spotify:artist:1SlAqzb3uAE8VESvSEIHC8","spotify:artist:75WikmVsKD8rhCCS0FJbhr","spotify:artist:1tr8buvJ7TK5UOD0DUfcND","spotify:artist:1Evb9PN8WwJ24aPV98o6wE","spotify:artist:1eatK1Zgmq5aDPdIIgUeCr","spotify:artist:5UvlXUPDnw4ZPITjKPN4bt","spotify:artist:1BSbatZxYuF7I71bbxQ6Rx","spotify:artist:3KFVpJymIEONoQTJppvUua","spotify:artist:3yq03EMnaOqVDFjua655nv","spotify:artist:1Z0f5jRRQzFS7acsaNbnxr","spotify:artist:4vbjkgnj8kFUTcu4tESoGO","spotify:artist:6ZwPz1B35r7EC8SyAvDha7","spotify:artist:5YKiu1bUqWGKL1NEIHfYDN","spotify:artist:02KFnEoYSknbPol7Tb9RBW","spotify:artist:6vskQAUMFb94q1xd14w1OF","spotify:artist:0mXo7iQ95lDlcZdCPEJYyh","spotify:artist:5njAynPPzwutQXEG894dUC","spotify:artist:3pCKDpEOw3sdFpAvOMYGca","spotify:artist:0DqRHkDMhaO1GAgN3qgSNj","spotify:artist:4OiZ3exasorVXYnDkFiIFR","spotify:artist:6JrdfUcEX6u9kF2MygtHz1","spotify:artist:6IIg70SIT5Mm75AexgAHpM","spotify:artist:5EQqBabP07LWC2cSWXv5Vh","spotify:artist:0bR6kgsxaq6C27nJKqt6Fy","spotify:artist:5oqM3Dtn8lvnPeqHK59vv5","spotify:artist:4Xfei8BCPubXEtzs6mCEin","spotify:artist:5u8SPrPF3l59v0u2RWuOEh","spotify:artist:5BRpanfwVkYrRe8nMZXJ1m","spotify:artist:02qgJVEsAr75Rak0PMhkDU","spotify:artist:0gatKtnZM9k8c6TzmaWh2r","spotify:artist:66nxrvK8KbgWNFY4PmOxkE","spotify:artist:4MfJiaWvv1JRoovI4WKdbE","spotify:artist:0FGmPrjBl5F0GnvIOlY609","spotify:artist:0jL5iQmyh5HsvMWUnBZ7yW","spotify:artist:1ebOVFziOV5WA9nWMtzQGQ"]



path = os.getcwd()+'/Bands'

print ("The current working directory is %s" % path)


# Loop
while True:
    # Main Menu
    #just for fun
    print()
    print(">>> Welcome to Spotipy " + displayName + "!")
    print(">>> You have " + str(followers) + " followers.")
    print()
    print("0 - Search for an artist")
    print("1 - exit")
    print()
    choice = input("Your choice: ")
    
    if choice == "0":
        print()
        for i in bands:
            print("################################################################")
           

            searchQuery = i
            print()
            spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
            # Get search results
            #searchResults = spotifyObject.search(searchQuery,1,0,"artist")
            searchResults = spotify.artist(i)
            #print(json.dumps(searchResults, sort_keys=True, indent=4))

            artist = searchResults['name']

            print("Band name:",artist)

            newdir = path+'/'+artist
            try:
                os.mkdir(newdir)
            except OSError:
                print ("Creation of the directory %s failed" % newdir)
            else:
                print ("Successfully created the directory %s " % newdir)
                os.chdir(newdir)
            

            # Extract album data
            print("-----------------Albums------------------")
            albumResults = spotifyObject.artist_albums(i,album_type='album')
            #print(json.dumps(albumResults, sort_keys=True, indent=4))
            albumResults = albumResults['items']
            print("Albums:")
            for item in albumResults:
                albumName = item['name']
                print("    -",item['name'])
                albumID = item['id']
                albumArt = item['images'][0]['url']
                print("             Album art")
                print("                 ",albumArt)
                image_url = item['images'][0]['url']
                # Open the url image, set stream to True, this will return the stream content.
                resp = requests.get(image_url, stream=True)
                # Open a local file with wb ( write binary ) permission.
                local_file = open(albumName+'_'+item['release_date']+'.jpg', 'wb')
                # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
                resp.raw.decode_content = True
                # Copy the response stream raw data to local image file.
                shutil.copyfileobj(resp.raw, local_file)
                # Remove the image url response object.
                del resp
            #Extrat singles data
            print("IMPRIMIR CONTEUDO DE SINGLE")
            singleResults = spotifyObject.artist_albums(i,album_type='single')
            #print(json.dumps(singleResults, sort_keys=True, indent=4))
            singleResults = singleResults['items']
            for item in singleResults:
                singleName = item['name']
                print("    -",item['name'])
                singleID = item['id']
                singleArt = item['images'][0]['url']
                print("             Single art")
                print("                 ",singleArt)
                image_url = item['images'][0]['url']
                # Open the url image, set stream to True, this will return the stream content.
                resp = requests.get(image_url, stream=True)
                # Open a local file with wb ( write binary ) permission.
                local_file = open(albumName+'_'+item['release_date']+'.jpg', 'wb')
                # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
                resp.raw.decode_content = True
                # Copy the response stream raw data to local image file.
                shutil.copyfileobj(resp.raw, local_file)
                # Remove the image url response object.
                del resp




        os.chdir(path)

        print("################################################################")
    if choice == "1":
        break