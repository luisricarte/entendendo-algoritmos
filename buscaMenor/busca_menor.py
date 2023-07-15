def buscaMenor(array):
    if len(array) == 0:
        return []
    
    menor = array[0]
    if len(array) == 1:
        return menor
    else:
        for e in array:
            if menor > e:
                menor = e
        return menor
    

buscaMenor([3,2,1,5])
buscaMenor([])