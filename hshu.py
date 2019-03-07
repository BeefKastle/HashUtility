#!/usr/bin/env python3

# hshu.py

# Created by Andrew Slejzer on  2/21/19

# email 00266097@student.necc.edu
# ------------------------------------------------------------------ #

# Hash Utility (hshu) is a tool to create, and compare hash digests.

# ------------------------------------------------------------------ #

# Import Statements
import hsh_funct
import hsh_digest
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

    try:
        afile = open(args.in_file, 'rb')
        digest = hsh_digest.hsh_digest()
        digest.from_file = args.in_file
        if args.md5:
            digest.digest = hsh_funct.md5_hsh(afile)
        elif args.sha1:
            digest.digest = hsh_funct.sha1_hsh(afile)
        elif args.sha256:
            digest.digest = hsh_funct.sha256_hsh(afile)
        else:
            print("You shouldnt have gotten here!")

        afile.close()
    except(FileNotFoundError):
        print("No file or directory called ", args.in_file)

    if args.comp_file is not None:
        try:
            bfile = open(args.comp_file, 'r')
            print(bfile.read())
            bfile.close()

        except(FileNotFoundError):
            print("No file called ", args.comp_file)

    print(digest.from_file)
    print(digest.digest)

if __name__ == '__main__':
    main()
