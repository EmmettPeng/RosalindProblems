'''
Tool: Make every sequence in fasta file in one line
'''

def onelinefasta(fasta_file, output_file):
	with open(fasta_file, 'r') as file:
		new_fasta = {}
		for line in file:
			if line.startswith('>'):
				name = line.split()[0]
				new_fasta[name]=''
			else:
				new_fasta[name] = new_fasta[name] + line.replace('\n', '')
		#print(new_fasta)
	with open(output_file, 'w') as out:
		for i in new_fasta.keys():
			out.write(i)
			out.write('\n')
			out.write(new_fasta[i])
			out.write('\n')


onelinefasta("E:/Denglab/学习/Rosalind Problems/hello.fasta","E:/Denglab/学习/Rosalind Problems/output.fasta")
