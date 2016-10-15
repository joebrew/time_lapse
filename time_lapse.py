# https://ubuntuforums.org/showthread.php?t=2022316

import os
import time
import shutil
import sys
import platform
import subprocess

# Define whether speeding up or slowing down
slow_down = 1
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
# Make a renamed directory
print 'Step 1----------------------------------'
shutil.rmtree('renamed', ignore_errors=True)
os.mkdir('renamed')
# Copy 
os.system("counter = 1; ls -1tr *.JPG | while read filename; do cp $filename renamed/$(printf %04d $counter)_$filename; ((counter++)); done")
os.chdir('renamed')

# STEP 2
print 'Step 2----------------------------------'
shutil.rmtree('resized', ignore_errors=True)
os.mkdir('resized')
os.system("mogrify -path resized -resize 1920x1080! *.JPG")
os.chdir('resized')
# Remove the ! to keep the aspect ratio
# 4k = 3840 x 2160 | 3840x2160
# HD = 1920 x 1080 | 1920x1080
# Could also do parallel
# You can also use the mogrify from graphicsmagick package which is faster, I use it in combination with the command "parallel" in order to utilize all of my CPU cores and perform the resize much faster.
# Of course, you can use the command "parallel" with the imagemagick mogrify
# parallel --progress gm mogrify -quality 100 -output-directory resized -resize 1920x1080! ::: *.JPG # Similar as before, remove the exclamation mark in order to keep the aspect ratio.

# STEP 3
print 'Step 3----------------------------------'
# If you photos have noticeable flickering which is caused by slightly different exposure between taken photos, download the attached script, put it in the directory source_folder_of_pictures/renamed/resized/, make it executable and run it. The script will create a subdirectory "source_folder_of_pictures/renamed/resized/Deflickered" to store the processed photos.
# You can get the latest version of the script at https://github.com/cyberang3l/timela...e-deflicker.pl

# sudo apt-get install libfile-type-perl libterm-progressbar-perl
# chmod +x timelapse-deflicker.pl
# ./timelapse-deflicker.pl -h
# ./timelapse-deflicker.pl -v
# cd Deflickered

# STEP 4
print 'Step 4----------------------------------'
os.system("ffmpeg -r 25 -pattern_type glob -i '*.JPG' -c:v copy output.avi")
 # Change -r 25 to define the frame rate. 25 here means 25 fps.

# STEP 5 (skipping)
print 'Step 5----------------------------------'

# STEP 6 compress
print 'Step 6----------------------------------'
x =  "ffmpeg -i output.avi" + slow_down_clause + "-c:v libx264 -preset slow -crf 15 output-final.mkv"
os.system(x)

# Delete all the other files and move the final file to the input dir
shutil.copyfile('output-final.mkv', input_dir + '/output-final.mkv')
os.chdir(input_dir)
shutil.rmtree('renamed/resized', ignore_errors=True)
shutil.rmtree('renamed', ignore_errors=True)

# FINAL open up in nautilus
subprocess.Popen(["xdg-open", input_dir])