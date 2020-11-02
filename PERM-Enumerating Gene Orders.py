'''
	Rosalind Problems: Enumerating Gene Orders
	Problem ID: PERM
	http://rosalind.info/problems/perm/

	A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.

	Given: A positive integer n≤7.

	Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).
'''

def factorial(n):
	#do factorial calculation: n should be a positive integer
	if n==1:
		return 1
	else:
		return n*factorial(n-1)

def all_num(n):
	ori = []
	for i in range(n):
		ori.append(i+1)
	return ori


def permutations(arr, position, end):
	if position == end:
		#print(arr)
		for i in arr:
			if i!=arr[-1]:
				print(i, end=' ')
			else:
				print(i, end='\n')

	else:
		for index in range(position, end):
			arr[index], arr[position] = arr[position], arr[index]
			permutations(arr, position+1, end)
			arr[index], arr[position] = arr[position], arr[index]


print(factorial(7))
ori = all_num(7)
permutations(ori, 0, len(ori))