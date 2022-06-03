#!/usr/bin/env python3
#
# This picks # random movies from the NAS for indecisive people
import os, glob, json, sys
from random import randint

def count_movies_by_year(movies):
  movies_by_year = {}

  for i in range(len(movies)):
    # Input includes path info. This just grabs the containing folder since
    # some movies contain multiple parts
    title = movies[i].split('\\')[3].split('/')[2]
    # print('title =', title)

    # Extract the yyyy
    year = int(title[-5:-1])

    # Strip off the yyyy part
    title = title[:-7]

    if year not in movies_by_year:
      movies_by_year[year] = [title]
    else:
      movies_by_year[year].append(title)
  
  return movies_by_year

def get_year_weights(movies):
  year_weights = []
  for year in sorted(movies):
    entry = (len(movies[year]), year)
    year_weights.append(entry)
  
  return year_weights

def weighted_random(pairs):
  total = sum(pair[0] for pair in pairs)
  r = randint(1, total)
  for (weight, value) in pairs:
    r -= weight
    if r <= 0:
      return value

def main(argv):
  # NAS config stores info about the server
  f = open('nas_config.json')
  nas_config = json.load(f)
  f.close()

  # Get path to movies
  movies = os.path.join(nas_config['ebert']['movies'])
  # print('movie path =', movies)

  # Count just the mkv movies
  mkv_movies = glob.glob(movies + '//**/*.mkv', recursive=True)
  mkv_movies.sort()

  # Build up a dictionary of all the mkv movies using the year as key
  movies_by_year = count_movies_by_year(mkv_movies)
  
  # Get list of weights which is tuple of (count, year)
  year_weights = get_year_weights(movies_by_year)

  for i in range(int(argv)):
    # Pick a year at random (weighted based on movies/year count)
    year = weighted_random(year_weights)

    # How many movies are there from this year?
    movies_this_year = len(movies_by_year[year])

    # Select a movie randomly from the selected year
    selection = movies_by_year[year][randint(0, movies_this_year - 1)] + ' (' + str(year) + ')'
    print('%d: %s' % (i, selection))

main(sys.argv[1])