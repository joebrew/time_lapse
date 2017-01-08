# https://ubuntuforums.org/showthread.php?t=2022316

import os
import time
import shutil
import sys
import platform
import subprocess
import re

# Define whether speeding up or slowing down (1 = default)
slow_down = 5
# below 1 = fast
# above 1 = slow
if slow_down == 1:
    slow_down_clause = " "
else:
    slow_down_clause = ' -filter:v "setpts=' + str(slow_down) + '*PTS" '


# Work from this directory
os.chdir('/home/joebrew/Documents/time_lapse')
this_dir = os.getcwd()

# Get directory of photos
try:
    input_dir = sys.argv[1]
except:
    input_dir = this_dir

print input_dir

# Go to input dir
os.chdir(input_dir)
print 'This working directory: ' + os.getcwd()

# STEP 1
# # Make a renamed directory
# print 'Step 1----------------------------------'
# shutil.rmtree('renamed', ignore_errors=True)
# os.mkdir('renamed')
# # Copy 
# os.system("counter=1")
# os.system("ls -1tr *.JPG | while read filename; do cp $filename renamed/$(printf %04d $counter)_$filename;  done")
# os.chdir('renamed')

# # STEP 2
# print 'Step 2----------------------------------'
# shutil.rmtree('resized', ignore_errors=True)
# os.mkdir('resized')
# # os.system("mogrify -path resized -resize 1920x1080! *.JPG")
# # os.system("mogrify -path resized -resize 1920x1080 *.JPG")
# os.system("mogrify -path resized -resize 960x720 *.JPG")
# os.chdir('resized')

# # STEP 3
# print 'Step 3----------------------------------'
# # Copy and overwrite
# import shutil
# import os

# source = os.getcwd()
# dest = input_dir

# # Remove from original dir
# os.chdir(input_dir)
# filelist = [ f for f in os.listdir(input_dir) if f.endswith(".JPG") ]
# print filelist
# for f in filelist:
#     os.remove(f)

# # Move 
# os.chdir(source)
# files = os.listdir(source)

# for f in files:
#     shutil.move(f, dest)

# # Remove folder
# os.chdir(input_dir)
# shutil.rmtree('renamed', ignore_errors=True)

# STEP 4
# Print out the link text
print 'Step 4----------------------------------'

filelist = [ f for f in os.listdir(input_dir) if f.endswith(".JPG") ]

the_dir = input_dir[45:]
for f in filelist:
    the_text = '\n' + '<a href="' + the_dir + f + '"> <img border="0" src= "' + the_dir + f + '" width="200"></a>' + '\n'
    print the_text
