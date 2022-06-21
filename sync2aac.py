#!/usr/bin/env python3

import os, sys, subprocess, glob, time

def convert(cmd, input, output):
    process = subprocess.Popen([cmd, input, output], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
    while True:
        line = process.stderr.readline().rstrip();
        if not line:
            break

def main():
    # Get path to flac converter
    flac2aac = os.path.join('flac2aac.bat')
    # print('flac2aac =', flac2aac)

    # Get path to Music Center (flac files)
    src_dir = os.path.join('C:\\Users\\justi\\Music\\Music Center')
    # print('src_dir =', src_dir)

    # Get path to aac files
    dst_dir = os.path.join('C:\\Users\\justi\\Music\\music_center_aac')
    # print('dst_dir =', dst_dir)

    # Get list of flac files
    flac_files = glob.glob(src_dir + '//**/*.flac', recursive=True)

    # Keeps track of how many conversions have taken place
    conversion_count = 0

    start = time.time()
    for i in range(len(flac_files)):
        # Path to the FLAC file to convert
        src_file = flac_files[i]

        # Get relative path to src file
        rel_flac_path = os.path.relpath(src_file, src_dir)

        # Create relative path to dst file
        rel_aac_path = os.path.splitext(rel_flac_path)[0] + '.m4a'

        # Path to destination file
        dst_file = os.path.join(dst_dir, rel_aac_path)

        # We need to get the artist/album folder names out of the relative path. We can't do
        # a conversion if the folders the file will go into doesn't exist!
        info = rel_flac_path.split('\\')
        artist = os.path.join(dst_dir, info[0])
        album = os.path.join(artist, info[1])

        # Create the artist & album folders if needed
        if not os.path.exists(artist):
            os.mkdir(artist)
        if not os.path.exists(album):
            os.mkdir(album)
        
        # If the destination file doesn't exists or is older than the source convert it
        if not os.path.exists(dst_file):# or (os.path.getctime(dst_file) < os.path.getctime(src_file)):
            # Display the file being converted
            print('%d : %s' % (conversion_count, rel_aac_path))
            conversion_count += 1
            convert(flac2aac, src_file, dst_file)
    
    end = time.time()
    print('Conversion took %.2f s' % (end - start))

if __name__ == "__main__":
    main()