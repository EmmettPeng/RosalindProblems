"""
	Rosalind Problems: Finding a Spliced Motif

	Problem ID: SSEQ

	http://rosalind.info/problems/sseq/

	A subsequence of a string is a collection of symbols contained in order (though not necessarily contiguously) in the string (e.g., ACG is a subsequence of TATGCTAAGATC). The indices of a subsequence are the positions in the string at which the symbols of the subsequence appear; thus, the indices of ACG in TATGCTAAGATC can be represented by (2, 5, 9).

	As a substring can have multiple locations, a subsequence can have multiple collections of indices, and the same index can be reused in more than one appearance of the subsequence; for example, ACG is a subsequence of AACCGGTT in 8 different ways.

	Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.

	Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions exist, you may return any one.
"""

from os import device_encoding


def sseq(obj, sub):
	collector = {}  #Index List of A T C G
	for i in ['A','T','C','G']:
		collector[i] = [n for n in range(len(obj)) if obj.find(i, n) == n]
	dec_seq = []
	flag = 0
	for char in sub:
		if flag ==0:
			dec_seq.append(min(collector[char])+1)
			flag = 1
		else:
			for i in collector[char]:
				if i>dec_seq[-1]:
					dec_seq.append(i+1)
					break
				else:
					continue
	return collector, dec_seq


obj = 'GCATGACAAGAGGGATTCTTTTTGTAAAATATCGAAGTCCATTTTCCCCAGCTCCCACGCGCAGGACGCGCCCGTAGCCGCTTAATTATGGGCTCCTGCTCAGTTTATAAACCATGCCATAGGTCGATGGATGGAATAACCACTACCAGGGCCTCGTTCCGAGTTATGCGCTCTACAGGTACAAAACTGTGAAAGATCGTGACGACGGAGAGCCTCATCTCTTTTACATGACCGGTCGGAGCCAGCCGACTGCTCTCTAATGAGCGTTGTGAGTACATGGGTAGGACCTAGTTGAGATGTACGACTTGTGACCTCGCCCGCACGTACGCCAAGGCCCTCCGGACATCATGCGCGTCTACAACGTCCTCCAGGTGAGGTGTCTGCCGCTATCTAACATAAGATTTTTGTTTGCAGGTTATAACAGCTTACTAACGCAGGAGAACAGGCTGGGAACCCCATTTCACCTGCTTTACCCATCGTACTAAGGCATTCTTATGACGCTTCTCGCTAGAGAGGACGGTTTGTAGGTCAGGCCTAAGGATTACCGTTAATGGCCGATAAGCACTATAATCCCACGGAGGGATGATGTTGAGGCGATAGGAATCTTCAAGGGCCCCAGGTATGAAGTCAACTTAACGTGGAAGTCTTCAGTTGACTAACGAGAGTTTTGACAGCGGTTAGCGTAATCTATCAATAATTTTACAGTCCGCTCCAGGGGTTGGGACTTCTACCGAGGCGCACTACGCTCATCAATACCGTCCGGAATAGCATCTATAACTGAGTATGTATACAGTCAACTAGTTCGTGCCCAGCAGAACGTTTTTTAGTTTAGGCGTCCATCCCATCCCGGCTGAATGGCCTAGATTTCGAAATGCATCTAACATCCGACGCCTTCTTTCACATACGTCGGATCGAGCCGAATGTGA'
sub = 'GAGGTTAACCGGGCGTTACACCGCCGGTGCGCGCGAAAGAATCCAAGTGGTTAAAACTATGGGCACACATACAAGAAATCTACCACGCAAACT'
collector, dec_seq = sseq(obj, sub)
for num in dec_seq:
	print(num, end=' ')