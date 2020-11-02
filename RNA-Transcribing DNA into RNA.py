'''
Rosalind Problems: [RNA] Transcribing DNA into RNA
'''

seq = 'ATGGTCTACATAGCTGACAAACAGCACGTAGCATCTCGAGAGGCATATGGTCACATGTTCAAAGTTTGCGCCTAG'

seq_t =[]
for nt in seq:
	if nt == 'T':
		seq_t.append('U')
	else:
		seq_t.append(nt)
out = ''
for i in seq_t:
	out = out + i
print(out)
