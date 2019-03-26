# hsh_digest.py

# Created by Andrew Slejzer on  3/7/19

# email 00266097@student.necc.edu
# ------------------------------------------------------------------ #

# Class definition of an object to hold a hash digest of a file

import hsh_funct

class hsh_digest():


    def __init__(self):
        self.hash_type = ''
        self.digest = ''
        self.file_name = ''

    def set_file_name(self, file_name):
        self.file_name = file_name

    def set_hash_type(self, hash_type):
        self.hash_type = hash_type

    def generate_hash(self):
        pass
        #might move all the if logic about which hash to use and the calls to the generators here