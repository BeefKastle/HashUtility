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
    parser.add_argument("in_file", help="File to be hashed")
    hsh_group = parser.add_mutually_exclusive_group(required=True)
    hsh_group.add_argument("--md5", help="flag to select md5 hash function", action="store_true")
    hsh_group.add_argument("--sha1", help="Flag to select sha1 hash function", action="store_true")
    hsh_group.add_argument("--sha256", help="flag to select sha256 hash function", action="store_true")
    parser.add_argument("--comp_file", '-c', help="file containing only a hash to be compared to the in_file")
    parser.add_argument("--out_file", "-o", help="Flag to create a file containing the hash that was produced", action="store_true")
    args = parser.parse_args()

    # open the selected files to read
    if args.in_file is not None:
        afile = open(args.in_file, 'rb')
        print("running hash on", args.in_file)
    else:
        print("No file selected")

    if args.comp_file is not None:
        bfile = open(args.comp_file, 'r')
        print(bfile.read())

    # if block to call the selected hash function
    if args.md5:
        print(hsh_funct.md5_hsh(afile), args.in_file)
        print(args.md5)
    elif args.sha1:
        print(hsh_funct.sha1_hsh(afile), args.in_file)
    elif args.sha256:
        print(hsh_funct.sha256_hsh(afile), args.in_file)
    else:
        print("No hash function specified, nothing generated")

    # close the files that were opened
    if args.in_file is not None:
        afile.close()
    if args.comp_file is not None:
        bfile.close()


if __name__ == '__main__':
    main()
