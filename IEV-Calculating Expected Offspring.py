'''
Rosalind Problems: [GRPH] Overlap Graphs
'''

def expected_offspring(g1,g2,g3,g4,g5,g6):
	offspring = g1+g2+g3+g4*0.75+g5*0.5
	offspring = 2*offspring
	print(offspring)

expected_offspring(17965,16995,18446,19895,16182,16762)