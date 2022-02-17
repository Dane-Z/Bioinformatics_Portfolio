#!/usr/bin/env python3
#11ex03

#!/usr/bin/env python3
#11ex02

with open("e_coli_k12_dh10b.faa") as fasta:
    bases = {"A":0, "C":0, "D":0, "E":0, "F":0, "G":0, "H":0, "I":0, "K":0, "L":0, "M":0, "N":0, "P":0, "Q":0, "R":0, "S":0, "T":0, "V":0, "W":0, "Y":0}

    for line in fasta:
        if line.startswith(">" or "\n"):
            continue
        for char in line:
            if char in bases:
                bases[char] += 1
    total = float(sum(bases.values()))
    for key,val in bases.items():
        print("{}: {}, ({:.1%})".format(key,val, val / total))
