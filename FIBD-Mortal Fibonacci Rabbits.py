'''
Rosalind Problems: [FIBD] Mortal Fibonacci Rabbits
'''

def mortal_rabbit(t, m):
	'''
	t = months
	m = lifetime
	'''
	life_table = [0]*(m+1)
	life_table[0]=1
	for i in range(1, t):
		life_table[1:m+1] = life_table[0:m]
		#print(life_table)
		life_table[0] = sum(life_table[2:])
	return sum(life_table[:-1])


print(mortal_rabbit(100,20))