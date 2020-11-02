'''
	Rosalind Problems: Locating Restriction Sites

	Problem ID: REVP

	http://rosalind.info/problems/revp/

	A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC. See Figure 2.

	Given: A DNA string of length at most 1 kbp in FASTA format.

	Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.
'''

'''
def palindrome(s, k):
	#k must be even numbers
	test_pool = []
	palindrome_pairs = [('A','T'),('T','A'),('G','C'),('C','G')]
	for i in range(len(s)-k+1):
		test = s[i:i+k]
		#print(test)
		test_pool.append(test)
	print(test_pool)
	flag = 0
	for s in test_pool:
		if all((s[i],s[k-i-1]) in palindrome_pairs for i in range(int(k/2-1))):
			flag += 1
			print(flag,k)
		else:
			flag +=1
'''

def palindrome(s, k):
	#k must be even numbers
	palindrome_pairs = [('A','T'),('T','A'),('G','C'),('C','G')]
	for i in range(len(s)-k+1):
		test = s[i:i+k]
		if all((test[j],test[k-j-1]) in palindrome_pairs for j in range(k)):
			#print(test, i+1, k)
			print(i+1, k)


string = 'TATATACCGGCTGACCCTTCTAGTGAGAGCCCGAAGAGGTACAATCATCGCTCAGAGCGGGGAGCACGATGATATGCCCACTCAAAGCTCGCGCTATCCCCTTAGAGCACCGAGTATAAGACGGCCCCAAAGCACGGGTATCAGGGTAGCACGTAAAAGTCGTTGTTGTAAATTGGCGTCGCATTACCCTATTGCTCTGAAGTAAGCCAAAAAATCCGATGTTCGGTGTTGAATGTTCATGCAGCAGGCCCGAAAAATCTAGTTGAGTCAATACGATTGGCCCCCCGACCAGCACCTGAAGCGAACGTGTACCAGTGGCTCCCTACATAATCGTGCGACTAGGCTATCGCCACCTCTCACTTGTAGTGAACTACTCTCTAGTCCGCAGGCAGCTCACATACGATTTCTCATTACCTCCCAAGCGAGCATCACCAAGAGTAGGATCGATGTCGGCCCTGAAGGCCACTCTGGAACTACCTTAAATCTTTATGTCCGGACATCAAGGACAAGATTTAACCCTCCCTATAAGTTCAACGAGGAATGGCGCCGCGTGCACCGTGAGACTGTAAAAGCCGGCTGTTCGTTACTCCCTGGATGCAACCCAAGTCAAGTATGTTAAAAAATCCCGATATGATGTTTACAGTACGCGTCACGAAATTCTATAGTTAATCTTCGGGTATATATGCTGTCTTATTAATTAGTACGCATTGCGGGCATCCAGCAACCGTGGAGTACTCAAACTTCAAAGGGTCCGCCCTTATGCCATCAGTGGGACTTTCTACAGGTACAATCGGTCGTCTTAGCCGCATTAGCATTCCCACGTCGAGGCCCCTCTCGGAGCTGGTTGCATTATGGACTAGCATCGGTATGCGCGATACTTGGAAGCCTCCCCTTAATCATACAGGAGCCGTAGGTTCCAATATCAAGCGCGGGTCGACGAATCGGAATTCTAGGAGGATTATCTTTTATCAGGCGCACCGACGCTATA'
for i in range(4,14,2):
	palindrome(string, i)


