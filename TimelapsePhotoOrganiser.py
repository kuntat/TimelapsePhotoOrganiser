##
## TimelapsePhotoOrganiser.py
## TimelapsePhotoOrganiser
##
## Created by Kun Tat on 14/5/16.
##


from os import listdir, makedirs
from os.path import isfile, join, getmtime, isdir, exists
from time import ctime
from shutil import move
from GetImageWidthHeight import get_image_size
import errno

def mkdir_p(path):
    try:
        makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and isdir(path):
            pass
        else:
            raise        

##mypath = "/Users/kuntat/Desktop/new"
print "To make this script run faster, consider making sure the dimensions of \
all your files are the same and turn off the check for dimensions.\n\n"
mypath = raw_input("Enter directory: ")
assert exists(mypath), "I did not find the file at "+str(mypath)
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and not f.startswith('.')]


foldernumber = 1
lastmod = getmtime(join(mypath, onlyfiles[0]))
lastDimension = get_image_size(join(mypath, onlyfiles[0]))
mkdir_p(mypath + "/Timelapse%s" %foldernumber)

print "Moving your files for you..."

for f in onlyfiles:
    f = join(mypath, f)
    if (getmtime(f) - lastmod < 60.0 and lastDimension == get_image_size(f)):
        lastmod = getmtime(f)
    else:
        lastmod = getmtime(f)
        lastDimension = get_image_size(f)
        foldernumber += 1
        mkdir_p(mypath + "/Timelapse%s" %foldernumber)
    move(f, mypath + "/Timelapse%s" %foldernumber) 

print "Done!"
