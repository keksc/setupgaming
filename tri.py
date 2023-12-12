def tri_selection(T):
    for i in range(len(T)-1):
        indMin = i
        for j in range(i+1, len(T)):
            if(T[j]<T[indMin]):
                indMin = j
        T[indMin],T[i] = T[i],T[indMin]
    return T
    
print(tri_selection([10, 3, -4, 4, 4, 5, 4, 2, 3, 2, 4, 3, 4]))
