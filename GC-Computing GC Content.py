'''
Rosalind Problems: [GC] Computing GC Content
'''

def GC_content(file):
	with open(file, "r", encoding='utf-8') as fa:
		data = fa.read().splitlines()
		#print(data)
		fasta_dict = {}
		for line in data:
			if '>' in line:
				i = data.index(line)
				data_str2list = list(data[i])
				data_str2list.pop(0)
				data_str2list = ''.join(data_str2list)
				data[i] = str(data_str2list)
				fasta_dict[data[i]] = data[i+1]
		#print(fasta_dict)
		stat = {}
		gc=0
		for keys in fasta_dict:
			for i in fasta_dict[keys]:
				if i == 'C' or i == 'G':
					gc = gc + 1
			stat[keys] = float(format(gc/len(fasta_dict[keys])*100, '.5f'))
			gc=0
		#print(stat)
		print(max(stat,key=stat.get))
		print(stat[max(stat,key=stat.get)])


GC_content("E:/Denglab/学习/Rosalind Problems/hello.fasta")