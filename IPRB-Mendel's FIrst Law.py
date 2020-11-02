'''
Rosalind Problems: [IPRB] Mendel's First Law
'''

def domi_phenotype(k,m,n):
	#k=AA, m=Aa, n=aa
	sum = k+m+n
	#P(A_)=1-P(aa)=1-(aa*aa+Aa*Aa*1/4+Aa*aa*1/2+aa*Aa*1/2)
	prob = 1 - (n*(n-1)+m*(m-1)/4+m*n)/(sum*(sum-1))
	return prob

print(domi_phenotype(27,26,20))
#0.783333333