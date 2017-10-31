#!/usr/bin/env python
import os, sys, hashlib, urllib.request

def sha256(filename):
    blocksize = 65536
    hasher = hashlib.sha256()
    with open(filename, 'rb') as afile:
        buf = afile.read(blocksize)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(blocksize)
    return hasher.hexdigest()

def download(vnum):
    response = urllib.request.urlopen(dlurl + vnum + filetype)
    data = response.read()
    if vnum == oldvnum:
        filename = oldpackagefile
    else:
        filename = newpackagefile
    file_ = open(filename, 'wb')
    file_.write(data)
    file_.close()

#Check the input args
try:
    oldvnum=sys.argv[1]
    newvnum=sys.argv[2]
except IndexError:
    print("Usage: update.py [old version number] [new version number]")

#Definitions
package='mullvad'
dlurl='https://mullvad.net/media/client/mullvad-'
filetype='.tar.gz'
oldpackagefile=package + '-' + oldvnum + filetype
newpackagefile=package + '-' + newvnum + filetype

# Read in the file
with open('PKGBUILD', 'r') as file :
  filedata = file.read()

# Hash the old version
if os.path.exists(oldpackagefile)== True:
    oldhash=sha256(oldpackagefile)
    print(oldhash)
else:
    download(oldvnum)
    oldhash=sha256(oldpackagefile)
    print(oldhash)

# Hash the new version
download(newvnum)
newhash = sha256(newpackagefile)
print(newhash)

# Replace the target string
oldpkgver = 'pkgver=' + oldvnum
newpkgver = 'pkgver=' + newvnum

dic = { oldpkgver : newpkgver , oldhash : newhash }

for i, j in dic.items():
        filedata = filedata.replace(i, j)

# Write the file out again
with open('PKGBUILD', 'w') as file:
  file.write(filedata)
