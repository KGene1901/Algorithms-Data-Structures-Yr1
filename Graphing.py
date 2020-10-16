#adspractical17.py
#algorithms and data structures practical week 17
#matthew johnson 21 february 2013
#last revised 21 february 2019

#####################################################

"""
in the module Computational Thinking (CT) you will use the package
NetworkX to work with more complex graphs/networks, but in this module we will
only work with small graphs in order to illustrate the algorithms that we meet;
so we can represent them in python very simply

and in fact, in this practical, we will look only at the various ways of
representing graphs -- you will have the chance to implement Breadth-First
Search in CT

we will represent vertices by letters "A", "B", "C" etc. so we can represent
the whole vertex set by a string; for example

V = "ABCDEFGHIJKLM"

and we can represent each edge by a string containing two characters such as
"AB"; if the graph is undirected then "AB" and "BA" are different ways of
representing the same edge, if it is directed "AB" is an edge from "A" to "B"
and "BA" is an edge from "B" to "A"

for an edge array representation we will use lists; for example

E = ['AB', 'AC', 'AD', 'AE', 'BC', 'BF', 'BG', 'CG', 'CH', 'EI',
    'EJ', 'EK', 'EL', 'FL', 'GH', 'GI', 'GM', 'KL', 'KM']

or we can write

E = "AB AC AD AE BC BF BG CG CH EI EJ EK EL FL GH GI GM KL KM".split()

these are two ways of writing the same thing as the split function turns the
long string into a list of short strings; the spaces tell it where to break

for an adjacency list representation we will use a dictionary; the keys are
the vertices and the values are strings containing the neighbouring vertices;
for example

E = {'A': 'BCDE',
     'B': 'ACFG',
     'C': 'ABGH',
     'D': 'A',
     'E': 'AIJKL',
     'F': 'BL',
     'G': 'BCHIM',
     'H': 'CG',
     'I': 'EG',
     'J': 'E',
     'K': 'ELM',
     'L': 'EFK',
     'M': 'GK'}

finally for an adjacency matrix representation we use a list of lists; the jth
item in the ith list is 1 if there is an edge from the ith vertex to the jth
vertex; otherwise it is 0; for example

E = [[0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
     [1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
     [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
     [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]]

then we can define a graph as a triple

G = (V, E, False)

where the third value tells us whether or not the graph is directed

below are three functions

array_to_lists
lists_to_matrix
matrix_to_array

which take as their input a graph defined with one of the representations and
return the same graph using a different representation; complete the functions
and call the test functions to check their correctness
"""

###################################################

#we define the example graph that might be useful while you experiment;
#you can also use the graphs defined for the test functions; see below

V = "ABCDEFGHIJKLM"
E = "AB AC AD AE BC BF BG CG CH EI EJ EK EL FL GH GI GM KL KM".split()
G = (V, E, False)

# print(G)

###################################################

def array_to_lists(G):
    """takes a graph represented by a vertex set and edge array and returns
    adjacency lists as a dictionary
    test with function test1()"""
    V, E, directed = G
    #initialize dictionary
    L = {}

    for i in E:
        if i[0] not in L.keys():
            L[i[0]] = i[1]
        else:
            if i[1] not in L[i[0]]:
                L[i[0]]+=i[1]
        
        if directed == False:
            if i[1] not in L.keys():
                L[i[1]] = i[0]
            else:
                if i[0] not in L[i[1]]:
                    L[i[1]]+=i[0]
        else:
            if i[1] not in L.keys():
                L[i[1]] = ''
            
    # print(L)
    #your code here: put entries in L such that, for each vertex v in V,
    #L[v] is a string containing vertices adjacent to v

    #return graph with edge array replaced by adjacency lists
    return (V, L, directed)

###################################################

def lists_to_matrix(G):
    """takes a graph represented by a vertex set and adjacency lists and returns
    an adjacency matrix as list of lists
    test with function test2()"""
    V, E, directed = G
    #initialize matrix
    M = []
    x=0
    

    for ele in V:
        M.append([0]*len(V))

    for i in V:
        
        for count in range (0,len(V)):
            if V[count] in E[i]:
                M[x][count] = 1
            else:
                continue
        x+=1
    
    #your code here: put lists in M such that the ith list is the
    #ith row of the adjacency matrix for G

    #return graph with adjacency lists replaced by adjacency matrix
    return (V, M, directed)

# lists_to_matrix(G)
###################################################

def matrix_to_array(G):
    """takes a graph represented by a vertex set and adjacency matrix and returns
    an edge array as a list of two-character strings;
    test with function test3()"""
    V, E, directed = G
    #initialize array
    A = []
    x = 0

    for i in range (0, len(V)):
        for j in range (0, len(V)):
            if E[i][j] == 0:
                continue
            else:
                if directed == False:
                    if V[j]+V[i] in A:
                        continue

                A.append(V[i]+V[j])
                
    #your code here: put strings in A to represent each edge of G

    #return graph with adjacency matrix replaced by edge array
    return (V, A, directed)

###################################################

#the following two functions might prove useful

def print_lists(G):
    """takes a graph with adjacency list representation and prints the lists"""
    V, E, directed = G
    for vertex in V:
        n = ""
        for neighbour in E[vertex]:
            n += neighbour + ", " 
        print (vertex[0] + ": " + n[:-2])
        
def print_matrix(G):
    """takes a graph with adjacency matrix representation and prints it"""
    for row in G[1]: print ("".join([str(a) for a in row]))

###################################################

#graphs for test functions
v = "abcdefgh"
a = "ab ac ad bc de ef eg eh gh".split()
ad = "ab ac ad ba bc de ef eg eh gh".split()
l = {'a': 'bcd', 'c': 'ab', 'b': 'ac', 'e': 'dfgh', 'd': 'ae', 'g': 'eh', 'f': 'e', 'h': 'eg'}
ld = {'a': 'bcd', 'c': '', 'b': 'ac', 'e': 'fgh', 'd': 'e', 'g': 'h', 'f': '', 'h': ''}
m = [[0, 1, 1, 1, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 1, 1, 1], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 0, 1, 0]]
md = [[0, 1, 1, 1, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0]]
ga = (v, a, False)
gl = (v, l, False)
gm = (v, m, False)
gad = (v, ad, True)
gld = (v, ld, True)
gmd = (v, md, True)

###################################################

#tests

def test1():
    """tests array_to_lists"""
    #first for undirected graphs
    e = array_to_lists(ga)[1]
    #put each list in alphabetical order
    for u in v:
        n = list(e[u])
        n.sort()
        n = "".join(n)
        e[u] = n    
    assert gl[1] == e
    print ("array_to_list() works for undirected graphs")
    #now for directed graphs
    e = array_to_lists(gad)[1]
    #put each list in alphabetical order
    for u in v:
        n = list(e[u])
        n.sort()
        n = "".join(n)
        e[u] = n    
    assert gld[1] == e
    print ("and for directed graphs too")
    print ("all tests passed")
    
test1()

def test2():
    """tests lists_to_matrix"""
    #first for undirected graphs
    assert gm == lists_to_matrix(gl)
    print ("lists_to_matrix() works for undirected graphs")
    #now for directed graphs
    assert gmd == lists_to_matrix(gld)
    print ("and for directed graphs too")
    print ("all tests passed")

test2()    

def test3():
    """tests matrix_to_array"""
    #first for undirected graphs
    e = matrix_to_array(gm)[1]
    #put each two-character edge in alphabetical order
    #i.e "AB" rather than "BA"
    for i in range(len(e)):
        if e[i][0] > e[i][1]:
            e = e[:i] + [e[i][1]+e[i][0]] + e[i+1:]
    #now put the set of edges in alphabetical order
    e.sort()
    assert ga[1] == e
    print ("matrix_to_array() works for undirected graphs")
    #now for directed graphs
    e = matrix_to_array(gmd)[1]
    #put the set of edges in alphabetical order
    e.sort()
    assert gad[1] == e
    print ("and for directed graphs too")
    print ("all tests passed")

test3()