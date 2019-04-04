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
        self.file = None

    def set_file_name(self, file_name):
        self.file_name = file_name

    def set_hash_type(self, hash_type):
        self.hash_type = hash_type

    def generate_hash(self):
        if self.hash_type == "md5":
            self.digest = hsh_funct.md5_hsh(self.file)
        elif self.hash_type == "sha1":
            self.digest = hsh_funct.sha1_hsh(self.file)
        elif self.hash_type == "sha256":
            self.digest = hsh_funct.sha256_hsh(self.file)
        else:
            print("No hash type specified")