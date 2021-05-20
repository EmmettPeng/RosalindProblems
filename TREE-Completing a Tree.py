"""
	Rosalind Problems: Completing a Tree

	Problem ID: TREE

	http://rosalind.info/problems/tree/

	An undirected graph is connected if there is a path connecting any two nodes. A tree is a connected (undirected) graph containing no cycles; this definition forces the tree to have a branching structure organized around a central core of nodes, just like its living counterpart. See Figure 2.

    We have already grown familiar with trees in “Mendel's First Law”, where we introduced the probability tree diagram to visualize the outcomes of a random variable.

    In the creation of a phylogeny, taxa are encoded by the tree's leaves, or nodes having degree 1. A node of a tree having degree larger than 1 is called an internal node.

    Given: A positive integer n (n≤1000) and an adjacency list corresponding to a graph on n nodes that contains no cycles.

    Return: The minimum number of edges that can be added to the graph to produce a tree
"""

def fill_edge(f):
    with open(f, 'r') as file:
        get_first_line = 0
        no_nodes = 0
        modules = []
        #appearance = 0
        no_modules = 0
        for line in file:
            if get_first_line == 0:
                no_nodes = int(line.replace('\n',''))
                get_first_line = 1
            elif get_first_line == 1:
                line = line.replace('\n', '')
                line = line.split(' ')
                m,n = line[0], line[1]
                modules.append(m)
                modules.append(n)
                #appearance += 2
                no_modules += 1
            else:
                line = line.replace('\n', '')
                line = line.split(' ')
                m,n = line[0], line[1]
                if m in modules and n not in modules:
                    modules.append(n)
                    #appearance += 1
                elif m not in modules and n in modules:
                    modules.append(m)
                    #appearance += 1
                elif m not in modules and n not in modules:
                    modules.append(m)
                    modules.append(n)
                    #appearance += 2
                    no_modules += 1
                else:
                    continue
    
    return  no_modules+no_nodes-len(modules)-1
                


def main():
    file_dir = 'E:\\迅雷下载\\rosalind_tree.txt'
    print(fill_edge(file_dir))

if __name__ == '__main__':
    main()

