'''
Rosalind Problems: [CONS] Consensus and Profile
'''

def consensus(fasta_file):
	counter = {'A': [], 'C': [], 'G': [], 'T': []}
	with open(fasta_file) as file:
		data = file.read().splitlines()
		#print(type(data)) <list>
		for line in data:
			if '>' in line:
				data.pop(data.index(line))
		#print(data[0][0])
		for i in range(len(data[0])):
			for keys in counter:
				counter[keys].append(0)
				#print(counter)
			for j in range(len(data)):
				if data[j][i] == 'A':
					counter['A'][i] += 1
				elif data[j][i] == 'C':
					counter['C'][i] += 1
				elif data[j][i] == 'G':
					counter['G'][i] += 1
				else:
					counter['T'][i] += 1
		print(counter)
		length = len(counter['A'])
		#print(length)  >>>8
		consensus_list = []
		for i in range(length):
			most = max(counter['A'][i], counter['C'][i], counter['G'][i], counter['T'][i])
			#print(most)
			for j in counter.keys():
				if counter[j][i] == most:
					consensus_list.append(j)
					break #this is to prevent output multiple nucleotides in one spot
		consensus_string = ''.join(consensus_list)
		print(consensus_string)
		for nt in ['A', 'C', 'G', 'T']:
			print(nt + ':', end = ' ')
			for i in range(len(counter['A'])):
				print(counter[nt][i], end = ' ')
			print('\n')
			
consensus("E:/Denglab/学习/Rosalind Problems/output.fasta")
