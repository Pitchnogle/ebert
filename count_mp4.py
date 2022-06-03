#!/usr/bin/env python3
#
# This counts the number of mp4 movies on the NAS
#
# Written by: Justin Hadella (pitchnogle@gmail.com)
import os, glob, json

def main():
  # NAS config stores info about the server
  f = open('nas_config.json')
  nas_config = json.load(f)
  f.close()

  # Get path to movies
  movies = os.path.join(nas_config['ebert']['movies'])
  # print('movie path =', movies)

  # Count just the mp4 movies
  mp4_movies = glob.glob(movies + '//**/*.mp4', recursive=True)
  print(len(mp4_movies))

main()