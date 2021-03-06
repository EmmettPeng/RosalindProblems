"""
	Rosalind Problems: Transitions and Transversions

	Problem ID: TRAN

	http://rosalind.info/problems/tran/

	For DNA strings s1 and s2 having the same length, their transition/transversion ratio R(s1,s2) is the ratio of the total number of transitions to the total number of transversions, where symbol substitutions are inferred from mismatched corresponding symbols as when calculating Hamming distance (see “Counting Point Mutations”).

    Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).

    Return: The transition/transversion ratio R(s1,s2).
"""


def hamming(s1,s2):
    if len(s1) != len(s2):
        #print('Error: Two sequences do not share the same length!')
        return 0
    else:
        hmd = 0  #define hamming distance
        transition = 0
        #transversion = 0
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            else:
                hmd += 1
                #Decide transition or transversion with ASCII code of A(65), C(67), G(71) and T(84)
                if abs(ord(s1[i])-ord(s2[i])) == 6 or abs(ord(s1[i])-ord(s2[i])) == 17:
                    transition += 1
        transversion = hmd - transition
        print('Hamming distance: {}'.format(hmd))
        print('Transition: {0}; Transversion: {1}'.format(transition, transversion))
        print('Transition/Transversion Ratio: {:.11f}'.format(transition/transversion))
        return 1

def main():
    s1 = 'TTGTCCGTGATGGGTCTTCGTTTTCCAAATGTTAGGGCGTCTTCGAAAGCAATTTTCGCCAAGGAGATTTGTCTTCCTTGCAATATGCTGACCCCGTCTTCGTAATGCGTTCGGGTTGATGCGTTCTGAGTCGTTGATGCTCGGGGGTCTCGAGCCCGTGGTACCACTTCTGCTCCAAAGTGCCTGACCCAAAATATTTGAACTGAACATCGTCCATTATGCGGCGGGCTCTGTGTTTCACCAGTCCTTCTTTTCAATATGATACCTATGACCTTGTCCTGGCCACCGGGTTGTTTCCCTTACATCCACTGTAGAGGGCCCCGTCGTGAGCGGGCCCTGCGGTATGCAGGTGACAGCGCGCTGTCCACTGACCAACAGCCCACAATGATACAATTCTCGCAATTATATACCGCTTTTTACTGAGTACATGTTAACATGGCGGGTGGTGTCCTTCCCGGACCCCACATTTACGATCGTGACTGAATGGCGGCCCGCATGACTAGTCTGGATGTAACACGGCGACGTGCACGGACTTTAGTCATTAAAACTAACCCCGGCGTACACCAGTCGCCGGTACAGCGCAGAGCTGAACATCGGCTCTGGTCCACTTTGCGGAAAAAGTCGGCATCTCCATATCGTAGTGTGAGATAAGGTGGTCGCCTTGCATAGAATGTACTATAGGGCTGTTCCCTTGTTAATAGTCACAGTCTATATCTGCGAATGCTTACGGCTCCTGGGTGCGAAACCTGTTCCCAGGGACCCTTACCAATTCTTTCATACCATCATCTAACCGTGTGGTATGTAGGGCCGGTTGCTTCACCTTCAAACG'
    s2 = 'GTGTCTATAATGGGCCTTCGTCTAACAGATGTTAGGGCGCCCCTGAAGGCAATCTCCGCTAGGTGGATCTGCCTTCCTTCCACAATGCTGACCCCATCTTCATAACGAGTTCGAGTCAAAGTGGTATGAGTCGTTGATGCCCGGTAGTCTCGGGCCCTTGGTACCACTTTTGCGCTGAAGTGCTCGATCCTCGGTGCTAAGATTGGGCATCGTCCATTATGCGGCAGGCTCTACGCATCTCTGTGTCCTCTATTATATCCGATACCTGTGACCACTACCTGGTCTTCGGGTTGTCTCCTTTACACCTCCCGTATAAGGTCCCAACCTGAGCCGGCACCTCGCTATGCAGTCCACACCGCGCTGTCTAGCAATCAGCAGCCCAAGATTCTACAGCTCCTGTAAACACATCCCGCTTTTCACTAGGTACTTGCTGACGTGACGGGGGGCATCCTTGCCAAACCACATGTTTACGGTTGCTCATGAATAGCATTCCGTGTGTCTAGTGTGCAGGTAACGTGGCGATGTGCGCGAACCCCAGTCTTTAGAACTACTCCCGGCAAACAACAATCGAGGGGGCGACGCAGAGCTGGGCATCGGTTCTGACCTACTTTGCAGGAAGAGTCGAGGACTCCGTCTCATAGCGTGATGTGTGGTAGCCGCGTTACATAAAATCCGTTACTGTGTTGTTTCTTCTTTGCTAGCTACTACCCAAATCTGCGAGTGCCTTCAGCTGTTTGGCGTGGGACCTGTTATCAAGCACTCTTGCCAGTCCTTTCTGTAGAGCATTTAACCATACAGTATGTGGATCGGGTTATTTAGTCTCTAAGCG'
    if hamming(s1,s2) == 0:
        print('Error: Two sequences do not share the same length!')

if __name__ == '__main__':
	main()