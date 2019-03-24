#!/usr/bin/env python3

# hshu.py

# Created by Andrew Slejzer on  2/21/19

# email 00266097@student.necc.edu
# ------------------------------------------------------------------ #

# Hash Utility (hshu) is a tool to create, and compare hash digests.

# ------------------------------------------------------------------ #

# Import Statements
import hsh_funct
import argparse
from hsh_digest import hsh_digest


def compare_hash(comp_digest, comp_file):
    for line in comp_file:
        if line.__contains__(comp_digest.digest):
            return True
    return False

def compare_hash_line_count(comp_digest, comp_file):
    line_count = 1
    for line in comp_file:
        if line.__contains__(comp_digest.digest):
            return line_count
        line_count = line_count + 1
    line_count = 0
    return line_count


def main():
    # Argument parsing block, may move to its own module
    parser = argparse.ArgumentParser()
    parser.add_argument("in_file", help="File to be hashed")
    hsh_group = parser.add_mutually_exclusive_group(required=True)
    hsh_group.add_argument("--md5", help="flag to select md5 hash function", action="store_true")
    hsh_group.add_argument("--sha1", help="Flag to select sha1 hash function", action="store_true")
    hsh_group.add_argument("--sha256", help="flag to select sha256 hash function", action="store_true")
    parser.add_argument("--comp_file", '-c', help="file containing only a hash to be compared to the in_file")
    parser.add_argument("--out_file", "-o", help="Flag to create a file containing the hash that was produced",
                        action="store_true")
    parser.add_argument("--verbose", '-v', help="flag to make command run with lots of text output",
                        action="store_true")

    args = parser.parse_args()  # object that contains all of the arguments passed to the program

    try:
        digest_store = hsh_digest()  # create an object to store the hash and file name as strings

        if args.verbose: print("Attempting to open:", args.in_file)
        afile = open(args.in_file, 'rb')
        if args.verbose: print("Sucessfully opened:", args.in_file)

        digest_store.file_name = args.in_file  # assign the file name as the in_file the user specified

        # if block to check which hash to use and assign the digest to the storage object
        if args.md5:
            if args.verbose: print("Running MD5 hash on:", args.in_file)

            digest_store.digest = hsh_funct.md5_hsh(afile)

            if args.verbose: print("Produced hash:\n", digest_store.digest, args.in_file)

        elif args.sha1:
            if args.verbose: print("Running SHA1 hash on:", args.in_file)

            digest_store.digest = hsh_funct.sha1_hsh(afile)

            if args.verbose: print("Produced hash:\n", digest_store.digest, args.in_file)

        elif args.sha256:
            if args.verbose: print("Running SHA256 hash on:", args.in_file)

            digest_store.digest = hsh_funct.sha256_hsh(afile)

            if args.verbose: print("Produced hash:\n", digest_store.digest, args.in_file)

        if args.verbose: print("Closing:", args.in_file)
        afile.close()

    except FileNotFoundError:
        print("No file or directory called ", args.in_file)

    if args.comp_file is not None:
        try:
            if args.verbose: print("Attempting to open:", args.comp_file)

            bfile = open(args.comp_file, 'r')

            if args.verbose: print("Sucessfuly opened:", args.comp_file)

            print("Comparing the hash digest of", args.in_file, "with the contents of", args.comp_file)

            if (compare_hash(digest_store, bfile)):
                print("The hash of", args.in_file, "is in", args.comp_file)

            else:
                print("The hash is not in the file")

            if args.verbose: print("Closing: ", args.comp_file)

            bfile.close()

        except FileNotFoundError:
            print("No file called ", args.comp_file)

    if args.out_file:
        try:
            out_file = open("%s.digest" % digest_store.file_name, "w+")
            out_file.write("%s ---------------- %s" % (digest_store.digest, digest_store.file_name))

        except:
            print("An error occured in creating the outfile")

    if not args.verbose:
        print("%s ---------------- %s" % (digest_store.digest, digest_store.file_name))


if __name__ == '__main__':
    main()
