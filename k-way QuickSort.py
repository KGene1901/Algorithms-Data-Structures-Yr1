import sys

def read_input(filename):   # reading inputs from command line
    A = []

    try:
        myfile = open(filename, 'r')
    except OSError:
        print('cannot open', filename)
        sys.exit(0)

    for line in myfile:
        A = A + [int(line.strip())]
    myfile.close()
    return A 

def partition(A,k): # partitions list of numbers into k+1 parts with k pivots
    pivot=[]
    sortListA=[]
    count=0
    P1=1
    P2=2
    if k<=0:
        return False

    else:
        for i in range(len(A)-1,len(A)-k-1,-1): # taking the k right most elements
            pivot.append(A[i])
            A.remove(A[i])
            pivot = insertionsort(pivot) # insertion sort on pivots

        for m in pivot:
            sortListA.append(m) # inserting pivot into final list

        # lines 36-42: creating partitions in between all k pivots
        sortListA=[[]] + sortListA
        sortListA.append([])
        while sortListA[P1]!=[] and sortListA[P2] != []:
            sortListA = sortListA[:P2] + [[]] + sortListA[P2:] # using list concantation to split the list to add "[]" in between two pivots
            P1+=2
            P2+=2

        for ele in A:
            count=0
            if ele<pivot[0]:
                sortListA[0].append(ele)    # inserting number less than the smallest pivot
            elif ele>pivot[len(pivot)-1]:
                sortListA[len(sortListA)-1].append(ele) # inserting number more than the largest pivot
            else:
                while ele>pivot[count]: # lines 51-55: inserting numbers in between pivots 
                    count+=1
                else:
                    index = sortListA.index(pivot[count-1]) 
                    sortListA[index+1].append(ele)
        
    return sortListA


def quicksort(A, k):
    if k<=0:
        return False
    if len(A)==1:
        return A    # an list of length 1 is already sorted (trivial)

    elif len(A)<=(2*k):   # insertionsort on any list of length 2k or less
        return insertionsort(A)

    else:
        sorted = partition(A,k) 
        for ele in sorted:
            if ele==[] or isinstance(ele, int): # ignores pivots
                continue
            else:
                sorted[sorted.index(ele)] = quicksort(ele,k)    # quicksort is called recursively on the k+1 parts
            
        sorted_list = []
        for sublist in sorted:  # lines 79-84: list flattening
            if isinstance(sublist,int):
                sorted_list.append(sublist)
            else:
                for item in sublist:
                    sorted_list.append(item)
       
        return sorted_list  # sorted list is returned


def insertionsort(A):   # pretty trivial insertionsort
    for j in range (1, len(A)):
        current = A[j]  
        prev = j-1
        while prev>=0 and current < A[prev]:    # swaps position of two numbers if prev>current 
            A[prev+1]=A[prev]
            prev-=1

        A[prev+1] = current 

    return A    # returns sorted list

def main(): # main function to call
    k = int(sys.argv[1])    # takes input as an integer
    filename = sys.argv[2]  # takes input as a data file
    A = read_input(filename)    
    print(quicksort(A, k))  # final output is produced
    

if __name__ == "__main__":
    main() 