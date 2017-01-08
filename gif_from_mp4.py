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

# Get file
try:
    the_file = sys.argv[1]
except:
    the_file = this_dir

print the_file
sub_file = os.path.basename(the_file)

# Bring file onto desktop
if os.path.dirname(the_file) == '~/Desktop' or os.path.dirname(the_file) == '/home/joebrew/Desktop':
    pass
else:
    shutil.copyfile(the_file, '/home/joebrew/Desktop/' + sub_file)

# Go to desktop
os.chdir('/home/joebrew/Desktop')

# Make a frames directory
shutil.rmtree('frames', ignore_errors=True)
os.mkdir('frames')
print os.getcwd()
print sub_file


deconstruct_text = "ffmpeg -i " + sub_file + " -r 5 'frames/frame-%03d.jpg'"
os.system(deconstruct_text)
os.chdir('frames')

os.system("convert -delay 20 -loop 0 *.jpg myimage.gif")
os.system("convert myimage.gif -coalesce temporary.gif")
os.system("convert -size 1920x1080 temporary.gif -resize 512x288 smaller.gif")
shutil.copyfile('smaller.gif', '/home/joebrew/Desktop/the_gif.gif')
subprocess.Popen(["xdg-open", '/home/joebrew/Desktop/the_gif.gif'])