#!/usr/bin/env python3

# hshu.py

# Created by Andrew Slejzer on  2/21/19

# email 00266097@student.necc.edu
# ------------------------------------------------------------------ #

# Hash Utility (hshu) is a tool to create, and compare hash digests.

# ------------------------------------------------------------------ #

# Import Statements
import hsh_funct
import sys
import argparse


def main():
    # Argument parsing block, may move to its own module
    parser = argparse.ArgumentParser()
    hsh_group = parser.add_mutually_exclusive_group()
    parser.add_argument("in_file", help="File to be hashed")
    hsh_group.add_argument("--md5", help="flag to select md5 hash function", action="store_true")
    hsh_group.add_argument("--sha1", help="Flag to select sha1 hash function", action="store_true")
    hsh_group.add_argument("--sha256", help="flag to select sha256 hash function", action="store_true")
    parser.add_argument("--comp_file", '-c', help="file containing only a hash to be compared to the in_file")
    args = parser.parse_args()

    # print the file that the program has selected to run the hash on
    print("running hash on", args.in_file)

    # open the selected files to read
    afile = open(args.in_file, 'rb')
    if args.comp_file is not None:
        bfile = open(args.comp_file, 'r')
        print(bfile.read())

    # if block to call the selected hash function
    if args.md5:
        print(hsh_funct.md5_hsh(afile))
    elif args.sha1:
        print(hsh_funct.sha1_hsh(afile))
    elif args.sha256:
        print(hsh_funct.sha256_hsh(afile))
    else:
        print("No hash function specified, nothing generated")

    # close the file that was hashed
    afile.close()


if __name__ == '__main__':
    main()
