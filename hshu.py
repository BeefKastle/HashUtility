#!/usr/bin/env python3

# hshu.py

# Created by Andrew Slejzer on  2/21/19

# email 00266097@student.necc.edu
# ------------------------------------------------------------------ #

# Hash Utility (hshu) is a tool to create, and compare hash digests.

# ------------------------------------------------------------------ #

# Import Statements
import argparse
import hashlib


BLOCK_SIZE = 65536

def output_to_file(hasher, file_name):
    try:
        out_file = open("%s.digest" % file_name, "w+")
        tmpstring = hasher.hexdigest() + "----------------" + file_name + '\n'
        out_file.write(tmpstring)
        out_file.close()
        pass
    except:
        print("An error occurred in creating the outfile")


def append_to_file(hasher, file_name, append_file):
    try:
        app_file = open(append_file, 'a')
        tmpstring = hasher.hexdigest() + "----------------" + file_name + '\n'
        app_file.write(tmpstring)
    except:
        print("Error opening append file")

def output_to_console(hasher, file_name):
    print(hasher.hexdigest(), "----------------", file_name)




def compare_hash_file(hasher, file_name, comp_file):
    try:
        file = open(comp_file, 'r')
        for line in file:
            if line.__contains__(hasher.hexdigest()):
                file.close()
                print("The hash of ", file_name, " is in ", comp_file)
                return True
        file.close()
        print("The hash is not in the file ", comp_file)
        return False
    except FileNotFoundError:
        print("No such file: ", comp_file)
        return False

def compare_hash_string(hasher, file_name, comp_string):
    if comp_string == hasher.hexdigest():
        print("The hash matches the string provided.")
    else:
        print("The hash does not match the string provided.")



def main():
    # Argument parsing block
    parser = argparse.ArgumentParser()
    parser.add_argument("algorithm", help="specify algorithm to be used")
    parser.add_argument("in_file", help="File to be hashed")

    comp_group = parser.add_mutually_exclusive_group()
    file_group = parser.add_mutually_exclusive_group()
    comp_group.add_argument("--comp_file", '-c', help="selects file hash digests to be compared to the digest of in_file")
    comp_group.add_argument("--comp_string", '-s', help="takes a string as an argument and compares the hash generated to it.")
    file_group.add_argument("--out_file", "-o", help="Flag to create a file containing the hash that was produced",
                            action="store_true")
    file_group.add_argument("--append_file", '-A', help="Selects a file to append the hash output to")

    args = parser.parse_args()  # object that contains all of the arguments passed to the program

    # inital values for variables. Need to be declared here since theyre used in conditional statements first in the program
    algorithm = ''
    #in_file = args.in_file
    file_name = args.in_file

    if hashlib.algorithms_available.__contains__(args.algorithm):
        algorithm = args.algorithm
    else:
        while not hashlib.algorithms_available.__contains__(algorithm):
            algorithm = input("Please specify algorithm:")

    hasher = hashlib.new(algorithm)

    try:
        # open file specified and read it serially into the hasher
        in_file = open(file_name, 'rb')
        buffer = in_file.read(BLOCK_SIZE)
        while len(buffer) > 0:
            hasher.update(buffer)
            buffer = in_file.read(BLOCK_SIZE)
        in_file.close()
    except:
        print("file file not found error")

    # check if the user has specified a comparison file
    if args.comp_file is not None:
        print("Comparing the hash digest of", file_name, "with the contents of", args.comp_file)
        compare_hash_file(hasher, file_name, args.comp_file)
    elif args.comp_string is not None:
        pass
        compare_hash_string(hasher, file_name, args.comp_string)

    # check if user has specified that they want the output of the hash written to a file
    if args.out_file:
        output_to_file(hasher, file_name)

    elif args.append_file is not None:
        append_to_file(hasher, file_name, args.append_file)

    else:
        output_to_console(hasher, file_name)







if __name__ == '__main__':
    main()
