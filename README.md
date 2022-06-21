# ebert
A collection of utility programs for use with NAS hosting movies, albums, etc.

## Movie Tools

- [convert_mp4](convert_mp4.py)  
  Convert mp4 videos into mkv
- [count_mkv_year](count_mkv_year.py)  
  Counts all the mkv movies on the NAS by year and displays the counts
- [count_mp4](count_mp4.py)  
  Counts the number of mp4 movies on the NAS
- [list_mkv](list_mkv.py)  
  Lists all the mkv movies on the NAS
- [list_mp4](list_mp4.py)  
  Lists all the mp4 movies on the NAS
- [movieprep](movieprep.py)  
  Creates a folder for each file within and then moves the file into it. This is useful 
  to easily get a folder of movie files into an folder structure which is compatible with
  Plex. _Could use a better name..._
- [next_mp4](next_mp4.py)  
  Prints out the first mp4 movie found on the NAS
- [random_movie](random_movie.py)  
  Picks # random movies from the NAS for indecisive people

## Music Tools

- [flac2aac](flac2aac.bat)  
  Converts a FLAC audio file into an AAC audio file
- [random_album](random_album.py)  
  Selects a random album from the NAS
- [sync_music](sync_music.bat)  
  Synchronizes contents of Sony Music Center to the NAS to keep things up to date
- [sync2aac.py](sync2aac.py)  
  Synchronizes contents of Sony Music Center (containing FLAC files) to another folder
  on PC with converted AAC files. Existing AAC files will be updated if source files
  are newer.
