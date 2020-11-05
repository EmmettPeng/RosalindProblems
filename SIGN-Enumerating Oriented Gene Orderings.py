"""
	Rosalind Problems: Enumerating Oriented Gene Orderings

	Problem ID: SIGN

	http://rosalind.info/problems/sign/

	A signed permutation of length n is some ordering of the positive integers {1,2,…,n} in which each integer is then provided with either a positive or negative sign (for the sake of simplicity, we omit the positive sign). For example, π=(5,−3,−2,1,4) is a signed permutation of length 5.

	Given: A positive integer n≤6.

	Return: The total number of signed permutations of length n, followed by a list of all such permutations (you may list the signed permutations in any order).
"""

from itertools import product

def fac(x):
	if x==1:
		return x
	else:
		return x*fac(x-1)

def perm(n):
	elem = []
	visit = []
	for i in range(1,n+1,1):
		elem.append(i)
		visit.append(True)
	#print(elem)
	temp = [0*n for i in range(len(elem))]
	def dfs(pos):
		if pos == len(elem):
			f = open('perm.txt','a+')
			for i in temp:
				f.write(str(i)+' ')
			f.write('\n')
			f.close()
			return
		
		for x in range(len(elem)):
			if visit[x] == True:
				temp[pos] = elem[x]
				visit[x] = False
				dfs(pos+1)
				visit[x] = True
	dfs(0)

	f = open('perm.txt', 'r')
	data = f.readlines()
	f.close()
	data2 = []
	for lines in data:
		data2.append(lines.replace(' \n', ''))
	allperm = []
	for i in range(fac(n)):
		allperm.append([])
	#print(allperm)
	for i in range(len(data2)):
		for num in data2[i]:
			if num != ' ':
				allperm[i].append(int(num))
	#print(allperm)
	return allperm

def signed(alist):
	num = len(alist)
	ctrl = []
	neg_pos = product([1,-1],repeat=num)
	for i in neg_pos:
		ctrl.append(i)
	#print(ctrl)
	combination = [[] for i in range(2**num)]
	for i in ctrl:
		ind = ctrl.index(i)
		for x in alist:
			pos = alist.index(x)
			combination[ind].append(i[pos]*x)
	#print(combination)
	for i in combination:
		for j in i:
			if i.index(j) != num-1:
				print(j, end=' ')
			else:
				print(j, end='\n')


def main():
	#Given number
	N = 5

	permutations = perm(N)
	#signed([1,2,3])
	print(fac(N)*(2**N))
	for i in permutations:
		signed(i)

if __name__ == '__main__':
	main()