def hash_quartic(x):
    A = ["-"]*23        # initialise table A

    for k in x:
        i = ((4*k)+7) % 23      # h(k) function
        m = i
        count = 0      # initialising counter    

        while A[i] != "-":
            i = (m + (count**4)) % 23       # quartic probing function
            count+=1
            if count == 23:     # returns the table after 23 as max size of table has reached
                return A

        A[i] = k    # appends key to the table A
    return A

def hash_double(y):
    B = ["-"]*23 # initialise table B

    for k in y:
        i = ((4*k)+7) % 23  # h(k) function
        m = i
        count = 0   # initialise counter

        while B[i] != "-":
            i = (m + (count*(17 - (k % 17)))) % 23      # h'(k) function 
            count+=1
            if count == 23: # returns the table after 23 as max size of table has reached
                return B

        B[i] = k    # appends key to the table B
        
    return B


