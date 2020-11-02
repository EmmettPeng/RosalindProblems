'''
Rosalind Problems: [HAMM] Counting Point Mutations
'''

def align(template, seq):
	length = len(template)
	counter = 0
	for i in range(length):
		if template[i] != seq[i]:
			counter = counter+1
	return counter

temp = 'TATTGTATTCTTTATTCCACCCCCGGGCGGAACACCGAATTAGGCGAGTGGCGAGACATCGCGCCGGCCGCTCAGGACATAGGTTAATGCATTTTCGTGCCCACTCTGCCAGGGTTTCGGATCTTCGCTACTAGGCAGAACCCGTACGGCTTAGAGATGCTTCTAGCGGTGGTTCAAACTTCCTAAGATCCTCCCTGGACTCCGTCTCGGTATGCATTCGTATTCCCCCCATCCGGCACCATATGGATCGTTAGTCAGGTAAGGGCTTACTATGACTCTAACAGCATTAATGTCACATTGTCTGATATGCCCAATAGTCTGCTTACCATTCAGATGCCACCTGCTCTGGAACTGCCGTGGTTGAATACAGCGTTAGTAGCAATCGTACAACAGGCGGCCTAAGTACACAAGTGGTTCAGTAATTACTTATTCGTCGGATATTGCTGACACCCTTAGGACCCGTGTCACGCTTATAACAGATCTTTCTTAGCTCACACATTGTGACCTGTTCTCTCCTTCCGACTGACCCATAGATTGGCTCTTAATCATCTTGCGCTCAGTATAATGGATGCTAATGGCTCTACTTTTTTTGCTTCCCAGCTACACTGCGAATAATCGACGTGTATTGGTCTCGTCCATCAGCCACGCGATGGGATACTTAGATCCGGTCGTCTTCATTCACCTGCGCATTCCATTTGATCGGCCAGGGGTGCCTGATAACTGGGTGGCCAGAATGCGTGACCCTGTCCAACTCAGCACAGCTAGACGGTGGAGCCCAGAGATGACGTCCCGGGGGGTCGGAACTAAGTTGCGCACGTCACTCTTTCGGCATTCCGAGTCAGATGGCTAGATTCATCACTGAACCAGAGTAGCGTATGGAAACAATAACGCCAGCCTGCTCATAAACAAGGTGCTAACCAATCCCCATCTAAACCGCTGCTTT'
seq = 'TATTGTATTCTCCAGTCCTACGGCCTACGGGCCGCCTAACTCGGCGTGTGGCGGGATCTTGCGCGGGCCGCGAATGTCATCGCTTGAGGCATGTTTATCTGCTCATGTCCAGCGCTGCGGATAAATGTCTAGGAGCAGAACTCTTTCGGTCTACAAATGGCTGCAGTTACTGGTGAAAGTGGCTAAGATTTTCGCTATGTTGCGTATCGTAATCCGGCCTTTTTGCGGACTACGGGCAGCTTGTCGGCATGTAGTAGGGTATGGGCTAGATATAAGGCGAACCGGTCACCATTGGTAGTGCCTGATAGAATAAACAACCCTGTTACCTTCCTGTGACCCACGGGTCAGGAACACCCAAGGTTGTTTCTAGCCCCGGCGGGAAACAAAAAAGCGTCGCCAACTGTACTCTAGAGTTCCGGCAGCTGCCTATTCGTAGCGTATTGTTGACTCCCTAGGCACCAACGCCGCTGAACTAACACTTCTTAGGTAAATTAGCAAACTTATCCGTATCCAATTGTGCAAAGTAACTCGCACAGGCGTGTTACGAGGTATCCGGTCCCTACAATCTAGTCTATCGGCTTGGTTGTCTTTATTTCCCACATACAGGGCACATATTCGATGTGTAAAGCTCTCATCCATAAAGCGCGGGCCCCGCTGGTGTAATGCGCGCGTTTTCCCACATAACGGCTTGCACTCTGACGGGCCTGTCGGTCAGGGACTGAGATAGCCCAGTATGTGTGCACATGGCACAGACTGTGAAGCTTGATCGGGGTGACCAGGGATTAGCTCTCCCTTGATAGTGAGCAACATGTGAACGTTAAGCTGGGCGGTTCAAGCGAGCGTTAGGTTGTATCATCTTGGAGGTCCGAAAAGATATGGACTCGGGACGAGAGACCTGACTGTATACTAGGCATTATCACATTTCGTTCATGACCGTTCTTTA'
print(align(temp, seq))
