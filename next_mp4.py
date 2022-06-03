#!/usr/bin/env python3
#
# This script prints out the first mp4 movie found on the NAS
#
# Written by: Justin Hadella (pitchnogle@gmail.com)
import os, sys, subprocess, random, glob, json, time

def convert(cmd, input, output):
  process = subprocess.Popen([cmd, '-i', input, '-vcodec', 'copy', '-acodec', 'copy', output], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
  while True:
    line = process.stderr.readline().rstrip();
    if not line:
      break
    # print(line)

def process(i, movies_path, movies):
  # Pick the i'th movie
  movie = movies[i];
  
  # Strip off the .mp4 extension...
  movie = os.path.splitext(movie)[0]
  # print('movie =', movie)

  input = os.path.join(movies_path, movie, movie + '.mp4')
  # print('input =', input)
  
  print('%2d:\t%s' % (i, os.path.basename(input).split('.')[0]))

def run(argv):
  # NAS config stores info about the server
  f = open('nas_config.json')
  nas_config = json.load(f)
  f.close()

  # Get path to movies
  movies = os.path.join(nas_config['ebert']['movies'])
  # print('movie path =', movies)

  # Consider just the mp4 movies
  mp4_movies = glob.glob(movies + '//**/*.mp4', recursive=True)
  mp4_movies.sort()
  # print(mp4_movies)
  
  for i in range(int(argv)):
    process(i, movies, mp4_movies)

run(sys.argv[1])