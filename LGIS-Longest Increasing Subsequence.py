#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
	Rosalind Problems: Longest Increasing Subsequence

	Problem ID: LGIS

	http://rosalind.info/problems/lgis/

	A subsequence of a permutation is a collection of elements of the permutation in the order that they appear. For example, (5, 3, 4) is a subsequence of (5, 1, 3, 4, 2).

	A subsequence is increasing if the elements of the subsequence increase, and decreasing if the elements decrease. For example, given the permutation (8, 2, 1, 6, 5, 7, 4, 3, 9), an increasing subsequence is (2, 6, 7, 9), and a decreasing subsequence is (8, 6, 5, 4, 3). You may verify that these two subsequences are as long as possible.

	Given: A positive integer n≤10000 followed by a permutation π of length n.

	Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.
"""

def lis_dp(n, input_perm):
	perm = []
	dp = [1]*n
	comp = []
	perm0 = input_perm.split( )
	for i in perm0:
		perm.append(int(i))
	for i in range(n):
		if i == 0:
			continue
		else:
			for j in range(i):
				if perm[i]>perm[j]: # > LIS < LDS
					comp.append(dp[j])
				else:
					comp.append(0)
			flag = max(comp)
			comp = [] # comp array must be reset
		dp[i] = dp[i] + flag
	return max(dp), dp, perm #max(dp) is the length of LIS

def lis(perm, dp, dpmax):
	perm.reverse()
	dp.reverse()
	lis = []
	x = dpmax
	while(x>0):
		if x == dpmax:
			tmp_start = dp.index(x)
			lis.append(perm[tmp_start])
			tmp_dp = dp[tmp_start:]
			tmp_perm = perm[tmp_start:]
			x = x-1
		else:
			tmp_start = tmp_dp.index(x)
			lis.append(tmp_perm[tmp_start])
			tmp_dp = tmp_dp[tmp_start:]
			tmp_perm = tmp_perm[tmp_start:]
			x = x-1
	lis.reverse()
	return lis


dpmax, dp, perm = lis_dp(9, '8 2 1 6 5 7 4 3 9')
output = lis(perm, dp, dpmax)
for i in output:
	print(i, end=' ')



