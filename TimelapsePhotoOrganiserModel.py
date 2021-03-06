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
from GetImageWidthHeight import get_image_size
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


def organise(inputpath, checkDimensions):

    mypath = str(inputpath)
    print mypath
    print checkDimensions
    try:
        assert exists(mypath), "I did not find the folder at "+str(mypath)
    except AssertionError, e:
        return False
    sortedFiles = sorted_ls(mypath)
    onlyfiles = [f for f in sortedFiles if isfile(join(mypath, f)) and not f.startswith('.')]
    print len(onlyfiles)
    print "Moving your stuff for you..."
    foldernumber = 1
    try:
        lastmod = getmtime(join(mypath, onlyfiles[0]))
    except IndexError, e:
        return False
    if checkDimensions:
        lastDimension = get_image_size(join(mypath, onlyfiles[0]))
    mkdir_p(mypath + "/Timelapse%s" %foldernumber)

    for f in onlyfiles:
        f = join(mypath, f)
        if checkDimensions:
            if (getmtime(f) - lastmod < 60.0 and lastDimension == get_image_size(f)):
                lastmod = getmtime(f)
            else:
                lastmod = getmtime(f)
                lastDimension = get_image_size(f)
                foldernumber += 1
                mkdir_p(mypath + "/Timelapse%s" %foldernumber)
        else:
            if (getmtime(f) - lastmod < 60.0):
                lastmod = getmtime(f)
            else:
                lastmod = getmtime(f)
                foldernumber += 1
                mkdir_p(mypath + "/Timelapse%s" %foldernumber)
            
        move(f, mypath + "/Timelapse%s" %foldernumber)
    print "done!"

    return True
