'''
Rosalind Problems: [REVC] Complementing a Strand of DNA
'''

seq = 'TCAGAAGTATGTGGGGCCCCCGTCCGGCCTGGAATTTAGCGCTATGAGTAACGTGGCGTGGATCGCCATGCATGTAGGTCACAGTTCACACTTAGCCTCATGCCATTCTCTCGGCAAATCGCCGGTGCTTTAACATGATCGGAATCGGTGCGGAGCTCAAACTCAGCTAGGCAACACCTGTGTGTGCAGGGGGGCCACTGATAAAGTGCGGAGACCTCAGTACACTTTGAGGGCGCTTACCCGCTGCCTGATACGCAAGTGTCGTGAACCAGTCTTGGCCGGCCGGGTTACGTGCATCAACTCAGGTGACTGTACGTTTACTTCGTGGCAGAACGAATATTTTCTGGGTTAAAGTTCCGGAGCCTGTGACTCCAGTGTTCACACAGGGGACTTGACTACATCCCTTGATCAGCCAGAGTGGTCTGTTGTGCGCTCGGCATTAAGAATTCTGCTATGCTGCGATATGCAATATGATCATGGGCGCAGTTTCTTTAGGAGAGTCAATTCAGCACTACGGGTGCAGACTTCTCCGCAGCGCGCCTGCGGGGACAGGCACCCGTTAGGCGGTCGATATTTCATGATGGCGGGTCACAACCGGTAGACCTGACGTCTATATATGAGAGGCTGAAGAATTCAAACCTATGATGATTAAGCAAGACCCTTGCCTGTGAAATAGGTTTAGATGCAGTGGAGACCCCTGCGGTCAGCCCTATCACATCTCGAGTTTGTAGGTGGAGGGAAGGAGGCGAACACCATTCACAGCATCGCTCGATGGAAGGACAGGAACAGCTCCTGTCGTGCTCCCCCTTGATATCCCACCTACGTCCCCGAGGGTAACTTTGTCACCG'

seq_c = []
complement = {'C':'G', 'G':'C', 'A':'T', 'T':'A'}
for nt in seq:
	seq_c.append(complement[nt])
#notice that the sequence needs to be reversed
seq_c.reverse()
seq_cr = "".join(seq_c)
out = ''
for i in seq_cr:
	out = out + i 
print(out)

