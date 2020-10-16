def fact(digit):            #calculating the child of the input number
    factorial={0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720, 7:5040, 8:40320, 9:362880}
    total=0
    for a in digit:
        total+=factorial[a] #summing factorial values based on the dictionary
    return (total)
def descs(x,y,z,desc,suit_desc,j):  #finding the descendants of the given input
    while x not in desc:            #checks if child already exists within the descendants calculated
        if len(desc)>y:
            break
        desc.append(x)
        j+=1                
        digit=list(map(int,str(desc[j])))
        x=fact(digit)
    else:
        if len(desc)==y:        #checks if the given input has k descendants
            suit_desc.append(z)    
def descendants(n1,n2,k): #main function which calls everything else
    suit_desc=[]
    for m in range (n1,n2):
        desc=[]                 #reintialising array to be used repeatedly throughout the loop
        j=-1                            
        digit=list(map(int,str(m)))     #splits integer into individual digits in a list structure
        x = fact(digit) 
        descs(x,k,m,desc,suit_desc,j)
    return(len(suit_desc))

