##
## TimelapsePhotoOrganiser.py
## TimelapsePhotoOrganiser
##
## Created by Kun Tat on 26/8/16.
##


from os import listdir, makedirs, stat
from os.path import isfile, join, getmtime, isdir, exists
from time import ctime
from shutil import move
import errno

import profile

def mkdir_p(path):
    try:
        makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and isdir(path):
            pass
        else:
            return False
        
def sorted_ls(path):
    mtime = lambda f: stat(join(path, f)).st_mtime
    return list(sorted(listdir(path), key=mtime))

print "To make this script run faster, consider making sure the dimensions of \
all your files are the same and turn off the check for dimensions.\n\n"
mypath = raw_input("Enter directory: ")

mypath = str(mypath)
print mypath
assert exists(mypath), "I did not find the folder at "+str(mypath)
sortedFiles = sorted_ls(mypath)
onlyfiles = [f for f in sortedFiles if isfile(join(mypath, f)) and not f.startswith('.')]
print len(onlyfiles)
print "Moving your stuff for you..."
lastname = (onlyfiles[0])[0:4]
    
mkdir_p(mypath + "/" + (onlyfiles[0])[0:4])

for onefile in onlyfiles:
    f = join(mypath, onefile)
    if (onefile[0:4] == lastname):
        lastname = onefile[0:4]
    else:
        lastmod = onefile[0:4]
        mkdir_p(mypath + "/" + onefile[0:4])
    move(f, (mypath + "/" + onefile[0:4]))
print "done!"


