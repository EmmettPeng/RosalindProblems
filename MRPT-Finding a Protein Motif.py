'''
Rosalind Problems: [MRPT] Finding a Protein Motif
'''

from urllib.request import urlretrieve
import re

def get_accession(inputfile):
	with open(inputfile, "r", encoding="utf-8") as f:
		accession = f.read().splitlines()
	#print(accession)
	return(accession)
	
def download_fasta(accession):
	print("Retrieving download information for " + accession)
	url_address = "http://www.uniprot.org/uniprot/" + accession + ".fasta"
	url_filename = accession + ".fasta"
	urlretrieve(url_address, url_filename)
	print(accession +" downloaded successfully!")
	#downloaded files are multiline fasta files. Should be converted to singleline fasta files first.
	singleline(url_filename)
	print(accession +" fasta file standardized!")

def find_motif(fasta_file):
	fasta_file2 = fasta_file + '.fasta'
	with open(fasta_file2, "r", encoding="utf-8") as f:
		data = f.read().splitlines()
		name = fasta_file2.split('.')[0]
		ids, seqs = data[0], data[1]
		regex =r'N[^P][ST][^P]'
		index = [0]
		new_index = 0
		while(re.search(regex, seqs[index[-1]:]) != None):
			reg = re.search(regex, seqs[index[-1]:]).span()
			new_index = new_index + reg[0] + 1
			#print(new_index)
			index.append(new_index)
		index.pop(0)
		#print(index)
		if index != []:
			print(fasta_file)
			for i in index:
				if i != index[-1]:
					print(i, end = ' ')
				else:
					print(i, end = '\n')

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

#accession_list = get_accession("E:/Denglab/学习/Rosalind Problems/accessionID.txt")
#for i in accession_list:
#	download_fasta(i)
if __name__ == '__main__':
	accession_list = get_accession('accessionID.txt')
	for i in accession_list:
		download_fasta(i)
	for i in accession_list:
		find_motif(i)