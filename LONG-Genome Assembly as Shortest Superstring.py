"""
	Rosalind Problems: Genome Assembly as Shortest Superstring

	Problem ID: LONG

	http://rosalind.info/problems/long/

	For a collection of strings, a larger string containing every one of the smaller strings as a substring is called a superstring.

	By the assumption of parsimony, a shortest possible superstring over a collection of reads serves as a candidate chromosome.

	Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format (which represent reads deriving from the same strand of a single linear chromosome).

	The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.

	Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome)

"""
'''
#traverse all permutations: too slow and memory load is too high

def shortestSuperstring(seq):
	length = len(seq)
	overlap_pool = [[0] * length for x in range(length)]
	#print(overlap_pool)
	original = {}
	for i, x in enumerate(seq):
		original[i] = x
		for j, y in enumerate(seq):
			if i!=j:
				for ans in range(min(len(x),len(y)), -1, -1):
					if x.endswith(y[:ans]):
						overlap_pool[i][j] = ans
						break
	print('Overlap matrix is:')
	for i in overlap_pool:
		print(i)
	#overlap_pool[i][j] is the number of max overlap characters. seq[i] gives suffix and seq[j] gives prefix.
	#print(original)

	keys = [i for i in original.keys()]
	#full permutation: build all paths
	def perm(data):
		if len(data) == 1:
			return [data]
		r = []
		for i in range(len(data)):
			s = data[:i] + data[i+1:]
			p = perm(s)
			for x in p:
				r.append(data[i:i+1]+x)
		return r

	paths = {}
	for k,v in enumerate(perm(keys)):
		paths.update({k:v})
		print(paths)

	print(paths)

	scoreboard = {}
	score = 0
	for path in paths.keys():
		for i in range(len(paths[path])-1):
			if overlap_pool[paths[path][i]][paths[path][i+1]] > 5:
				score = score + overlap_pool[paths[path][i]][paths[path][i+1]]
			else:
				break
		scoreboard.update({path:score})
		score = 0

	print('Scoreboard:')
	print(scoreboard) #Overlap chars for every possible path

	#pick the highest score and get its path
	highest_score = max(scoreboard.values())
	best_path_no = [k for k,v in scoreboard.items() if v == highest_score]
	best_path = []
	for x in best_path_no:
		best_path.append(paths[x])
	#print('best path is:')
	#print(best_path)
	for alter_path in best_path:
		overlap_path = []
		for i in range(len(alter_path)-1):
			overlap_path.append(overlap_pool[alter_path[i]][alter_path[i+1]])
		#print(overlap_path)
		for i in alter_path:
			if alter_path.index(i) == 0:
				print(seq[i], end='')
			else:
				print(seq[i][overlap_path[i-1]:], end='')

def getfile(file):
	with open(file, 'r') as f:
		seq = []
		for line in f:
			if line.startswith('>'):
				pass
			else:
				seq.append(line.replace('\n',''))
		return seq

seq = getfile('output.fasta')
shortestSuperstring(seq)

'''

def getfile(file):
	with open(file, 'r') as f:
		seq = []
		for line in f:
			if line.startswith('>'):
				pass
			else:
				seq.append(line.replace('\n',''))
		return seq

def concatenate_overlap(str1, str2):
	less = min(len(str1), len(str2))
	for i in range(less, int(less/2), -1):
		if str1[-i:] == str2[:i]: #suffix of str1 == prefix of str2 (max overlap)
			return str1 + str2[i:]
			break
		elif str2[-i:] == str1[:i]:
			return str2 + str1[i:]
			break

seq = getfile('output.fasta')
#print(seq)

while(len(seq)>1):
	saver = (float('inf'),'','')
	for x in seq[1:]:
		temp = concatenate_overlap(seq[0],x)
		if temp and (len(temp) < saver[0]):
			saver = (len(temp), temp, x)

	seq[0] = saver[1]
	seq.pop(seq.index(saver[2]))

print(len(seq))
