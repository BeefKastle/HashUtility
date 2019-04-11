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


    def set_file(self, *args):
        if len(args) == 0:
            try:
                user_temp = input("please enter file name: ")
                self.file = open(user_temp, 'rb')
                self.file_name = user_temp
            except FileNotFoundError:
                print("No such file exists")
                self.set_file()
        elif len(args) == 1:
            try:
                self.file = open(args[0], 'rb')
                self.file_name = args[0]
            except FileNotFoundError:
                print("No such file exists")
                self.set_file()
        else:
            print("something went wrong")




    def set_hash_type(self, *args):
        if len(args) == 0:
            self.hash_type = input("Please enter hash type: ")
        elif len(args) == 1:
            self.hash_type = args[0]
        else:
            print("something went wrong")




    def generate_hash(self):
        if self.hash_type == "md5":
            self.digest = hsh_funct.md5_hsh(self.file)
        elif self.hash_type == "sha1":
            self.digest = hsh_funct.sha1_hsh(self.file)
        elif self.hash_type == "sha256":
            self.digest = hsh_funct.sha256_hsh(self.file)
        else:
            print("Incorrect hash type specified")
            self.set_hash_type()
            self.generate_hash()