#!/usr/bin/env python3
#
# This script uses `ffmpeg` to convert mp4 videos into mkv
import os, sys, subprocess, random, glob, json, time

def convert(cmd, input, output):
  process = subprocess.Popen([cmd, '-i', input, '-vcodec', 'copy', '-acodec', 'copy', output], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
  while True:
    line = process.stderr.readline().rstrip();
    if not line:
      break
    # print(line)

def process(i, movies_path, movies, ffmpeg):
  # Pick the i'th movie
  movie = movies[i]
  
  # Strip off the .mp4 extension...
  movie = os.path.splitext(movie)[0]
  # print('movie =', movie)

  input = os.path.join(movies_path, movie, movie + '.mp4')
  # print('input =', input)
  
  output = os.path.join(movie + '.mkv')
  # print('output =', output)

  # Start the conversion
  start = time.time()
  convert(ffmpeg, input, output)
  end = time.time()
  
  print('%2d:\t(%.2f s)\t%s' % (i, end - start, os.path.basename(output).split('.')[0]))

def run(argv):
  # NAS config stores info about the server
  f = open('nas_config.json')
  nas_config = json.load(f)
  f.close()

  # Get path to movies
  movies = os.path.join(nas_config['ebert']['movies'])
  # print('movie path =', movies)

  # Get path to ffmpeg.exe
  ffmpeg = os.path.join(nas_config['ffmpeg'])
  # print('ffmpeg =', ffmpeg)

  # Consider just the mp4 movies
  mp4_movies = glob.glob(movies + '//**/*.mp4', recursive=True)
  mp4_movies.sort()
  # print('mp4_movies =', mp4_movies)
  
  for i in range(int(argv)):
    process(i, movies, mp4_movies, ffmpeg)

run(sys.argv[1])