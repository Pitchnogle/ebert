#!/usr/bin/env python3
#
# This counts all the mkv movies on the NAS by year
import os, glob, json

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

def main():
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
  
  for year in sorted(movies_by_year):
    print('%s\t%s' % (year, len(movies_by_year[year])))

main()