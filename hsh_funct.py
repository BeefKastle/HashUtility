# hsh_funct.py

# Created by Andrew Slejzer on  2/21/19

# email 00266097@student.necc.edu
# ------------------------------------------------------------------ #

# this file sets up the various hashing functions so they canbe called from the main file(hshu.py)

# ------------------------------------------------------------------ #

import hashlib

# set size of memory blocks to load from the file
# When loading random files of any size its good to seperate the data
# into blocks and process it, this uses less memory.
BLOCK_SIZE = 65536


# each hahsing function is essentially the same
# get passed a file
def md5_hsh(afile):
    hasher = hashlib.md5()              # create a hasher object
    buff = afile.read(BLOCK_SIZE)       # add the first block of the file to the buffer
    while len(buff) > 0:                # while there is data in the buffer:
        hasher.update(buff)             # update the hasher with the data
        buff = afile.read(BLOCK_SIZE)   # read the next block of data into the buffer
    return(hasher.hexdigest())          # return the hexdigest of the file loaded into the hasher

def sha1_hsh(afile):
    hasher = hashlib.sha1()
    buff = afile.read(BLOCK_SIZE)
    while len(buff) > 0:
        hasher.update(buff)
        buff = afile.read(BLOCK_SIZE)
    return(hasher.hexdigest())

def sha256_hsh(afile):
    hasher = hashlib.sha256()
    buff = afile.read(BLOCK_SIZE)
    while len(buff) > 0:
        hasher.update(buff)
        buff = afile.read(BLOCK_SIZE)
    return(hasher.hexdigest())

# could a better way of doing this with the arguments is to create a class to be used in main?
# create an object that gets passed the file location and hash flag, generates the hash and holds it
# how would that work with the comparison file.
