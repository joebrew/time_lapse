# https://ubuntuforums.org/showthread.php?t=2022316

import os
import time
import shutil
import sys
import platform
import subprocess

# Work from this directory
os.chdir('/home/joebrew/Documents/time_lapse')
this_dir = os.getcwd()

# Get speed
human_speed = sys.argv[2]
speed = 1.0 / int(human_speed)
print 'Computer speed is ' + str(speed)
print 'Speed is ' + human_speed + 'x'

# Get file
try:
    the_file = sys.argv[1]
except:
    the_file = this_dir

print the_file
sub_file = os.path.basename(the_file)
#
# Bring file onto desktop
if os.path.dirname(the_file) == '~/Desktop' or os.path.dirname(the_file) == '/home/joebrew/Desktop':
    pass
else:
    shutil.copyfile(the_file, '/home/joebrew/Desktop/' + sub_file)

# Go to desktop
os.chdir('/home/joebrew/Desktop')
#
# # Speed up the video
name_without_ext = os.path.splitext(sub_file)[0]

speed_up = 'ffmpeg -i ' + sub_file + ' -an -filter:v "setpts=' + str(speed) + '*PTS" ' + name_without_ext + '_' + human_speed + '.mp4'
print speed_up
os.system(speed_up)
#
#
subprocess.Popen(["xdg-open", '/home/joebrew/Desktop/' + name_without_ext + '_' + human_speed + '.mp4'])
