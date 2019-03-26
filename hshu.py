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
import hsh_digest

bool_verbose = False

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

def verbose(verb):
    # function to clean up the rest of the code. lets verbose output be written in a single function call and string
    # Example:
    # verbose("Here's what it would say if --verbose is set")
    global bool_verbose
    if bool_verbose:
        print(verb)

def main():
    # Argument parsing block
    parser = argparse.ArgumentParser()
    parser.add_argument("in_file", help="File to be hashed")
    hsh_group = parser.add_mutually_exclusive_group(required=True)
    file_group = parser.add_mutually_exclusive_group()
    hsh_group.add_argument("--md5", help="flag to select md5 hash function", action="store_true")
    hsh_group.add_argument("--sha1", help="Flag to select sha1 hash function", action="store_true")
    hsh_group.add_argument("--sha256", help="flag to select sha256 hash function", action="store_true")
    parser.add_argument("--comp_file", '-c', help="selects file hash digests to be compared to the digest of in_file")
    file_group.add_argument("--out_file", "-o", help="Flag to create a file containing the hash that was produced",
                        action="store_true")
    parser.add_argument("--verbose", '-v', help="flag to make command run with lots of text output",
                        action="store_true")
    file_group.add_argument("--append_file", '-a', help="Selects a file to append the hash output to")

    args = parser.parse_args()  # object that contains all of the arguments passed to the program

    # check if the verbose flag was enabled and set global var accordingly
    if args.verbose:
        global bool_verbose
        bool_verbose = True

    # try block for opening file, generating a hash, and storing it
    try:
        digest_store = hsh_digest.hsh_digest()  # create an object to store the hash and file name as strings

        verbose("Attempting to open: %s" % args.in_file)
        afile = open(args.in_file, 'rb')
        verbose("Sucessfully opened: %s" % args.in_file)

        digest_store.file_name = args.in_file  # assign the file name as the in_file the user specified

        # if block to check which hash to use and assign the digest to the storage object
        if args.md5:
            verbose("Running MD5 hash on: %s" % args.in_file)

            digest_store.digest = hsh_funct.md5_hsh(afile)

        elif args.sha1:
            verbose("Running SHA1 hash on: %s" % args.in_file)

            digest_store.digest = hsh_funct.sha1_hsh(afile)

        elif args.sha256:
            verbose("Running SHA256 hash on: %s" % args.in_file)

            digest_store.digest = hsh_funct.sha256_hsh(afile)

        verbose("Closing: %s" % args.in_file)
        afile.close()

    except FileNotFoundError:
        print("No file or directory called ", args.in_file)

    # check if the user has specified a comparison file
    if args.comp_file is not None:
        # try block for opening comparison file
        try:
            verbose("Attempting to open: %s" % args.comp_file)

            bfile = open(args.comp_file, 'r')

            verbose("Sucessfuly opened: %s" % args.comp_file)

            print("Comparing the hash digest of", args.in_file, "with the contents of", args.comp_file)

            # if the hash generates is in the comparison file, say so
            if (compare_hash(digest_store, bfile)):
                print("The hash of", args.in_file, "is in", args.comp_file)

            else:
                print("The hash is not in the file")

            verbose("Closing: %s" % args.comp_file)

            bfile.close()

        except FileNotFoundError:
            print("No file called ", args.comp_file)

    # check if user has specified that they want the output of the hash written to a file
    if args.out_file:
        try:
            verbose("creating digest file: %s.digest" % digest_store.file_name)
            out_file = open("%s.digest" % digest_store.file_name, "w+")
            out_file.write("%s ---------------- %s\n" % (digest_store.digest, digest_store.file_name))
            out_file.close()

        except:
            print("An error occurred in creating the outfile")

    elif args.append_file is not None:
        try:
            verbose("opening append file")
            app_file = open(args.append_file, 'a')
            verbose("appending hash to file")
            app_file.write("%s ---------------- %s\n" % (digest_store.digest, digest_store.file_name))
        except:
            print("Error opening append file")

    else:
        verbose("generated hash:")
        print("%s ---------------- %s" % (digest_store.digest, digest_store.file_name))


if __name__ == '__main__':
    main()
