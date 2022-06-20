:: Script to convert a FLAC file into AAC file for portable devices
::
:: iPods can't play FLAC files, others can't play ALAC files...
:: However, most modern portables can play AAC files no problem.
::
:: Written by: Justin Hadella (pitchnogle@gmail.com)

:: Path to ffmpeg.exe
set prog="C:\Users\justi\Downloads\ffmpeg-4.4-full_build\bin\ffmpeg.exe"

:: %1 = the input file
:: %2 = the output file

:: Convert the FLAC into an AAC file
%prog% -i %1 -map a:0 -c:a aac -b:a 320k %2