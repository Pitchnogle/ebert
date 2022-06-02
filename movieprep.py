#!/usr/bin/env python3
#
# The function of this script was to help organize a folder which contains
# many individual movie files for use with plex, where each movie should 
# be in its own folder
#
# Handy script iterates through files in a directory, and for each file,
# creates a directory with the filename without the extension, and then
# moves the file into that directory
#
# For example, let's start with a directory with some files
# d:\>tree test /f
# Folder PATH listing
# Volume serial number is 000000AB 363F:A0E0
# D:\TEST
#     file1.avi
#     file2.avi
#     file3.avi
# 
# No subfolders exist
#
# After running the script, there will be a folder for each file, and
# each folder will contain the source file.
#
# d:\>python movieprep.py test
#
# Now, let's see what's happened
#
# d:\>tree test /f
# Folder PATH listing
# Volume serial number is 000000F3 363F:A0E0
# D:\TEST
# ├───file1
# │       file1.avi
# │
# ├───file2
# │       file2.avi
# │
# └───file3
#         file3.avi 

import os, sys, shutil

def createDirAndMoveFile(path, filename):
  dirname = filename[:-4]
  dst = os.path.join(path, dirname)
  os.mkdir(dst)
  src = os.path.join(path, filename)
  shutil.move(src, dst)
  
def main(argv):
  cwd = os.getcwd()
  path = os.path.join(cwd, argv)
  os.chdir(path)
  cwd = os.getcwd()
  for filename in os.listdir(path):
    createDirAndMoveFile(path, filename)
  
main(sys.argv[1])