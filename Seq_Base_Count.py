##Rosalind Module One
##Count Bases in a DNA sequence

#Counts all bases in a DNA seq.
file = open('./rosalind1.txt', 'r')
string = file.read()

bases = {"A":0, "C":0, "G":0, "T":0}
        
for char in dna:
    bases[char] += 1

print(bases["A"],bases["C"],bases["G"],bases["T"])
