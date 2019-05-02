# Hash Utility
Hash Utility is a tool for generating and comparing cryptographic hash digests.

## Usage
To use the script place it into the directory which contains the file that the that you want to generate a hash of. To run the file type the command:

`./hshu.py [algorithm] [file]`

Algorithm can be any algorithm provided by the python libraries installed on the machine. The program will stop and prompt the user to keep entering algorithms until they enter one that is valid.
Once the user has indicated a valid hash algorithm, the program will then try to open the file specified by the user, and once it has will generate the specified hash digest and output it to the console.

There are currently three flags that can be used with the script, only one may be used at a time:

### Output options

`-a [append_file];` Sets the program to not output any results to the console, but instead append the normal output to a file specified by the user. If there is no file of that name the program creates it and populates the first line with the generated hash.

### Comparison Options

`-c [comparison_file]`: sets the program to try to open a second file to read and compare the hash generated on the first file to the contents of the second. Writes a confirmation to the console if the hash is found in the file provided.

`-s [comparison_string]`: sets the program to compare the hash generated from the file selected to a string provided as an argument. It will only write a confirmation if the string provided matches the digest EXACTLY.



