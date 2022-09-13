from heapq import merge


def merge_bookings(b1, b2):
    b = []
    i, j = 0, 0

    while (i < len(b1) and j < len(b2)):
        I = b1[i]
        J = b2[j]
        # Case 1: rb1 starts before rb2 
        if I[1] < J[1]:
            s = I[1]
            k = I[0]
            # rb1 ends before or same as rb2 starts
            if I[2] <= J[1]:
                t = I[2]
                i += 1
            # rb1 ends after rb2 starts
            else:
                t = J[1]
                I[1] = J[1]

        # Case 2: rb1 starts at the same time as rb2
        elif I[1] == J[1]:
            s = I[1]
            k = I[0] + J[0]
            # rb1 ends same as rb2
            if I[2] == J[2]:
                t = I[2]
                i += 1
                j += 1
            # rb1 ends before rb2
            elif I[2] < J[2]:
                t = I[2]
                i += 1
                J[1] = I[2]
            # rb1 ends after rb2
            else:
                t = J[2]
                j += 1
                I[1] = J[2]
        
        # Case 3: rb1 starts after rb2
        else:
            s = J[1]
            k = J[0]
            t = I[1]
            # rb1 starts later or when rb2 ends
            if I[1] >= J[2]:
                t = J[2]
                j += 1
            # rb1 starts when rb2 is running
            else:    
                J[1] = I[1]
            
        b.append( [k,s,t] )

    while (i < len(b1)):
        b.append(b1[i])
        i += 1

    while (j < len(b2)):
        b.append(b2[j])
        j += 1
    
    return b

def satisfying_booking_listForm(R):

    B = []
    n = len(R)
    
    if n == 1:
        s,t = R[0]
        return [[1,s,t]]

    else:
        c = n // 2
        b1, b2 = R[0:c], R[c:n]
        L1 = satisfying_booking_listForm(b1)
        L2 = satisfying_booking_listForm(b2)
        B = merge_bookings(L1,L2)
    
    return B

def satisfying_booking(R):

    B = []
    for i in R:
        B.append(list(i))
    C = satisfying_booking_listForm(R)

    A = []
    for i in C:
        A.append(tuple(i))

    return tuple(A)