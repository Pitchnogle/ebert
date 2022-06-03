#!/usr/bin/env python3
#
# This selects a random album from the NAS
#
# On the NAS, music data is organized in the form:
# <music path>/<artist>/<title>
# 
# On Windows 10, an example folder name would be:
# '\\192.168.0.32\Music//Steve Martin\Let's Get Small\'
#
# Example Output:
# > python .\random_album.py      
# Various Artists - The Best Of Bond... James Bond
# > python .\random_album.py
# Iron Maiden - Killers
#
# Written by: Justin Hadella (pitchnogle@gmail.com)
import os, glob, json
from random import randint

def main():
  # NAS config stores info about the server
  f = open('nas_config.json')
  nas_config = json.load(f)
  f.close()

  # Get path to movies
  music_dir = os.path.join(nas_config['ebert']['music'])
  # print('music_dir =', music_dir)

  all_folders = glob.glob(music_dir + '//**/', recursive=True)

  albums = []
  for i in range(len(all_folders)):
    # Strip of the path info common to all albums
    folder = all_folders[i].split('//')[1:]
    # print('folder =', folder)

    # Split what's left to separate the artist/album
    info = folder[0].split('\\')
    
    # The above also gets us just the artist folder which we reject based
    # on the length. We want the artist and title
    if len(info) > 2:
      album = info[0] + ' - ' + info[1]
      albums.append(album)
  
  # Get a random album
  print(albums[randint(0, len(albums) - 1)])

main()