'''
Rosalind Problems: [LCSM] Finding a Shared Motif
'''

def sort_fasta(fasta_file):
	with open(fasta_file) as file:
		data = file.read().splitlines()
		fasta = {}
		for line in data:
			if line.startswith('>'):
				name = line
				fasta[name] = ''
			else:
				fasta[name] = fasta[name] + line
		fasta = sorted(fasta.items(), key=lambda i:len(i[1]))
		#fasta is a list made up of tuples
		return fasta


def shared_motif(fasta_file):
	fasta = sort_fasta(fasta_file)
	#print(fasta)
	fasta_sequence = []
	for i in fasta:
		fasta_sequence.append(fasta[fasta.index(i)][1])
	#print(fasta_sequence)
	max_try_len = len(fasta[0][1])
	shortest = fasta[0][1]
	#print(shortest[0:10])
	#list all k-mers of the shortest sequence, then test if they are in all other sequences
	kmer_list = []
	for length in reversed(range(max_try_len+1)):
		if length == 0:
			break
		kmer_sum = max_try_len - length +1
		#print(kmer_sum)
		for i in range(kmer_sum):
			kmer_list.append(shortest[i:i+length])
			#print(kmer_list)
	#here, kmer_list should contain all the kmer from the max-mer to the 1-mer
	#print(kmer_list)

	#for loop
	'''
	for kmer in kmer_list:
		checkboard = 0
		for check in fasta_sequence:
			if kmer in check:
				checkboard = checkboard + 1
				if checkboard == len(fasta):
					motif = kmer
					return motif
					break
	'''

	#all()
	for kmer in kmer_list:
		if all(kmer in check for check in fasta_sequence):
			motif = kmer
			return motif
			break

#@Pathfinder: I believe calling all() first involves computing the boolean values for all the elements in the list. This is much slower than calling break if the substring is not in any one DNA string. Goes to show that elegant-looking code isn't always fast code.
print(shared_motif("E:/Denglab/学习/Rosalind Problems/output.fasta"))
#("E:/Denglab/学习/Rosalind Problems/hello.fasta")