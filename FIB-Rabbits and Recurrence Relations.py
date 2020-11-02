'''
Rosalind Problems: [FIB] Rabbits and Recurrence Relations
'''

def fibonacciRabbits(n,k):
    F = [0,1,1]
    generation = 3
    while generation <= n:
        F.append(F[generation-1]+F[generation-2]*k)
        generation += 1
 
    return (F[n])

print(fibonacciRabbits(28,3))