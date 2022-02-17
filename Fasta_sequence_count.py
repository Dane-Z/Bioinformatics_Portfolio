#!/usr/bin/env python3
#Function accepts a filename, seeks for 'v' and returns the value of a count
def fasta_sequence_count(filename):
    count = 0
    for line in open(filename):
        if line.startwith('>'):
            count += 1
        return count
