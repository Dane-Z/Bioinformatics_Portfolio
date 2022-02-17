#!/usr/bin/env python3
#Class file
import re
from collections import defaultdict

class Repeat:

    def __init__(self, id=None, name=None, seq=None):
        self.id = id
        self.name = name
        self.seq = seq
#Gets ID, Latin name, and seq
    def get_fasta_in(self, file_path):
        for line in open(file_path):
            line = line.rstrip()

            if line.startswith(">"):
                t = re.match(">(\S+)\s*(\w+ \w+)", line)
                if t:
                    self.id = t.group(1)
                    self.name = t.group(2)
            else:
                if self.seq is None:
                    self.seq = line
                else:
                    self.seq += line

#Counts and displays triplets and % frequencies.
    def trip_count(self):
        dict = defaultdict(int)
        if len(self.seq) % 3 == 0:
            a = [i for i in self.seq]
            for i in range(len(self.seq)//3):
                cod = ''.join(a[(0+3*i):(3+3*i)])
                for base1 in ['A', 'T', 'G', 'C']:
                    for base2 in ['A', 'T', 'G', 'C']:
                        for base3 in ['A', 'T', 'G', 'C']:
                            trip = base1 + base2 + base3
                            if cod == trip:
                                dict[cod] += 1
            total = float(sum(dict.values()))
            for key in sorted(dict):
                print ("{0}: {1}, {2}%".format(key, dict[key], (dict[key] / total)*100))
        else:
            return "Invalid"
#Counts and displays a desired base received as input from the main
    def find_base(self, base):
        bases = {"A":0, "T":0, "C":0, "G":0}
        
        for char in self.seq:
            bases[char] += 1
        for key,val in bases.items():
            if key == base:
                return "Count = {}".format(val)
             
