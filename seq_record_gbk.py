from Bio import SeqIO
for seq_record in list(SeqIO.parse("ls_orchid.gbk", "genbank"))[:5]:
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))
