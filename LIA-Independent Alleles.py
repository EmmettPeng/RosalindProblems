'''
Rosalind Problems: [LIA] Independent Alleles
'''

def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

k = 5
N = 9
kk = 2**k
NN = 2**k

p = 0
while NN>=N:
	p = p + (factorial(kk)/(factorial(NN)*factorial(kk-NN))) *(0.25 ** NN) * (0.75 ** (kk-NN))
	NN -=1

print(round(p,3))