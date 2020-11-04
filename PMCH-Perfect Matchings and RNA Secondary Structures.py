"""
	Rosalind Problems: Perfect Matchings and RNA Secondary Structures

	Problem ID: PMCH

	http://rosalind.info/problems/pmch/

	Given: An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.

	Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s.
"""

with open('hello.fasta') as f:
	data = f.readlines()
	sequence = data[1:]
	seq = ''
	for line in sequence:
		seq = seq + line.replace('\n','')

au = seq.count('A')
gc = seq.count('G')

def fac(x):
	if x==1:
		return x
	else:
		return x*fac(x-1)

print(fac(au)*fac(gc))


