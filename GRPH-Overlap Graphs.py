'''
Rosalind Problems: [GRPH] Overlap Graphs
'''

def overlap(fasta_file, k):
	with open(fasta_file,'r') as file:
		data = file.read().splitlines()
		#print(data)
		names = []
		names2 = []
		seqs = []
		for line in data:
			if line.startswith('>'):
				names.append(line)
			else:
				seqs.append(line)
		#print(names, seqs)
		prefix_list = []
		suffix_list = []
		for i in names:
			i.strip('>')
			names2.append(i.strip('>'))
		names = names2
		#print(names)
		for i in range(len(names)):
			prefix_list.append(seqs[i][0:k])
			suffix_list.append(seqs[i][-k:-1] + seqs[i][-1])
		#print(prefix_list, suffix_list)
		for i in range(len(prefix_list)):
			for j in range(len(suffix_list)):
				if prefix_list[i] == suffix_list[j] and names[i] != names[j]:
					print(names[j], names[i], end = '\n')


overlap("E:/Denglab/学习/Rosalind Problems/output.fasta", 3)
