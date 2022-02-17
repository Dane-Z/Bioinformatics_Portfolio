##Rosalind Module Two
##Transcribing DNA into RNA
import re

#Transcribes DNA seq. into RNA seq.
file = open('/Users/Dane/Documents/IDLE/Rosalind/rosalindMA.txt')
t = file.readline().rstrip("\n")

complement = {'A':'A', 'T':'U','G':'G','C':'C'}
com_string = "".join(complement[char] for char in t)
print("DNA to RNA complement sequence: ", com_string)


                     
