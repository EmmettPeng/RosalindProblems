"""
	Rosalind Problems: Introduction to Random Strings

	Problem ID: PROB

	http://rosalind.info/problems/prob/

	Given: A DNA string s of length at most 100 bp and an array A containing at most 20 numbers between 0 and 1.

	Return: An array B having the same length as A in which B[k] represents the common logarithm of the probability that a random string constructed with the GC-content found in A[k] will match s exactly.
"""

from math import log10

seq = 'TAATAAGGCGCTACCACGACAGGATCCAACAGCGATCACTAGCAACATTCACCCGAATATTATCGTGCTTCAGCATAGCTCGC'
A = '0.080 0.124 0.202 0.213 0.277 0.347 0.369 0.429 0.515 0.563 0.582 0.669 0.687 0.776 0.841 0.859 0.910'.split(' ')
arrayA=[float(i) for i in A]

output = []
A_GC =[i/2 for i in arrayA]
A_AT =[(1-i)/2 for i in arrayA]

for i in range(len(arrayA)):
	GC = A_GC[i]
	AT = A_AT[i]
	probability = 0
	for j in seq:
		if j =='G' or j == 'C':
			probability = probability + log10(GC) # lg(xy) = lgx + lgy
		else:
			probability = probability + log10(AT)
	output.append(round(probability,3))

for x in output:
	print(x,end=' ')
print('\n')