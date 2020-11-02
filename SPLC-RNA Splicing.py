'''
	Rosalind Problems: RNA Splicing

	Problem ID: SPLC

	http://rosalind.info/problems/splc/

	After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.

	Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.

	Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)
'''

def transcibe(dna):
	seq_t =[]
	for nt in dna:
		if nt == 'T':
			seq_t.append('U')
		else:
			seq_t.append(nt)
	out = ''
	for i in seq_t:
		out = out + i
	return out

def translate(rnaseq):
	codon_table = { 'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V', \
					'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V', \
					'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V', \
					'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V', \
					'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A', \
					'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A', \
					'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A', \
					'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A', \
					'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D', \
					'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D', \
					'UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E', \
					'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E', \
					'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G', \
					'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G', \
					'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G', \
					'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'}
	length = len(rnaseq)
	proseq = []
	for i in range(0,length,3):
		triplet = rnaseq[i:i+3]
		if codon_table[str(triplet)] != 'Stop':
			proseq.append(codon_table[str(triplet)])
		else:
			break
	proseq = ''.join(proseq)
	return proseq

def rm_substr(s, sub):
	start = s.find(sub)
	end = len(sub) + start
	newstr = s[0:start] + s[end:]
	if sub not in newstr:
		return newstr
	else:
		return rm_substr(newstr, sub)

def singleline(fasta_file):
	with open(fasta_file, 'r') as file:
		new_fasta = {}
		for line in file:
			if line.startswith('>'):
				name = line.split()[0]
				new_fasta[name]=''
			else:
				new_fasta[name] = new_fasta[name] + line.replace('\n', '')
		#print(new_fasta)
	with open(fasta_file, 'w+') as out:
		key_list = list(new_fasta.keys())
		for i in new_fasta.keys():
			if i != key_list[-1]:
				out.write(i)
				out.write('\n')
				out.write(new_fasta[i])
				out.write('\n')
			else:
				out.write(i)
				out.write('\n')
				out.write(new_fasta[i])

def rm_introns(fasta):
	#The first sequence is the complete DNA sequence and others are introns to be spliced
	with open(fasta, 'r') as f:
		dat = f.read().splitlines()
		fasta = {}
		for line in dat:
			if line.startswith('>'):
				ind = dat.index(line)
				line = line[1:]
				fasta[line] = dat[ind+1]
		seqs = []
		for keys in fasta:
			seqs.append(fasta[keys])
		proc = seqs.pop(0)
		for i in seqs:
			if i in seqs:
				proc = rm_substr(proc, i)
		return proc

if __name__ == '__main__':
	singleline('hello.fasta')
	proc = rm_introns('hello.fasta')
	mrna = transcibe(proc)
	protein = translate(mrna)
	print(protein)
