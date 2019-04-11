#!/usr/bin/env python3

# hshu.py

# Created by Andrew Slejzer on  2/21/19

# email 00266097@student.necc.edu
# ------------------------------------------------------------------ #

# Hash Utility (hshu) is a tool to create, and compare hash digests.

# ------------------------------------------------------------------ #

# Import Statements
import argparse
import hsh_digest


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
    # Argument parsing block
    parser = argparse.ArgumentParser()
    parser.add_argument("--in_file", "-i", help="File to be hashed")
    file_group = parser.add_mutually_exclusive_group()
    parser.add_argument("--hash_type", '-t', help="specify hash type to be used here, supports \"md5\", \"sha1\", and \"sha256\"")
    parser.add_argument("--comp_file", '-c', help="selects file hash digests to be compared to the digest of in_file")
    file_group.add_argument("--out_file", "-o", help="Flag to create a file containing the hash that was produced",
                        action="store_true")
    file_group.add_argument("--append_file", '-a', help="Selects a file to append the hash output to")

    args = parser.parse_args()  # object that contains all of the arguments passed to the program

    digest_store = hsh_digest.hsh_digest()



    if args.in_file is not None:
        digest_store.set_file(args.in_file)
    else:
        digest_store.set_file()


    if args.hash_type is not None:                  # make sure the user specifies a hash type
        digest_store.set_hash_type(args.hash_type)  # set hash type from arguments
    else:
        # make the user enter a hash type
        digest_store.set_hash_type()

    digest_store.generate_hash()

    # check if the user has specified a comparison file
    if args.comp_file is not None:
        # try block for opening comparison file
        try:

            bfile = open(args.comp_file, 'r')

            print("Comparing the hash digest of", args.in_file, "with the contents of", args.comp_file)

            # if the hash generates is in the comparison file, say so
            if (compare_hash(digest_store, bfile)):
                print("The hash of", args.in_file, "is in", args.comp_file)

            else:
                print("The hash is not in the file")


            bfile.close()

        except FileNotFoundError:
            print("No file called ", args.comp_file)





    # check if user has specified that they want the output of the hash written to a file
    if args.out_file:
        try:
            out_file = open("%s.digest" % digest_store.file_name, "w+")
            out_file.write("%s ---------------- %s\n" % (digest_store.digest, digest_store.file_name))
            out_file.close()

        except:
            print("An error occurred in creating the outfile")

    elif args.append_file is not None:
        try:
            app_file = open(args.append_file, 'a')
            app_file.write("%s ---------------- %s\n" % (digest_store.digest, digest_store.file_name))
        except:
            print("Error opening append file")

    else:
        print("%s ---------------- %s" % (digest_store.digest, digest_store.file_name))







if __name__ == '__main__':
    main()
