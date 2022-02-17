#!/usr/bin/env python3
# Dane Zeeb

import module_class

def main():
    repeat = module_class.Repeat()
    repeat.get_fasta_in('test_fasta-1.fna')
    print("Sequence ID: {0}".format( repeat.id ))
    print("Latin Name : {0}".format(repeat.name ))
    repeat.trip_count()
    print("Occurences of base 'C' : {0}".format(repeat.find_base('C')))

if __name__ == '__main__':
    main()
