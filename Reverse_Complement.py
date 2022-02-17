##/usr/bin/env python3
# Rosalind module 3, Dane Zeeb
# Reverse complementing Oligonucleotide sequences
import re

file = open('/Users/Dane/Documents/IDLE/Rosalind/rosarevc.txt')
##oligo_str = file.readline().rstrip("\n")

def complement(oligo_str=None):

    complement = {'A':'T', 'C': 'G', 'T':'A', 'G':'C'}
    com_string = "".join(complement[char] for char in oligo_str)
    rev_com = com_string [::-1]
    print(rev_com)

print("This program will return the reverse complement of an Oligonucleotide sequence!")
while True:
    ##oligo_str = input("Please Input a Valid Oligonucleotide Sequence: ")
    oligo_str = file.readline().rstrip("\n")

    if re.search('(^[ACTG]+$)', oligo_str):
        complement(oligo_str)
    else:
        print("An invalid character was found, ending run.")
        break

print("Goodbye")

