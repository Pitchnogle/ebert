#!/usr/bin/env python3
#
# This lists all the mp4 movies on the NAS
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
  mp4_movies.sort()
  # print(len(mkv_movies))

  for i in range(len(mp4_movies)):
    # Title in form: 'movie title (yyyy)'
    title = os.path.basename(mp4_movies[i]).split('.')[0]
    # print('title =', title)

    # Extract the yyyy
    year = title[-5:-1]

    # Strip off the yyyy part
    title = title[:-7]

    print('%4d:\t%s\t%s' % (i, year, title))

main()