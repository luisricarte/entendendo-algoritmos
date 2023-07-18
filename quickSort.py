def quickSort(arr):
    if len(arr) < 2: #1 ou 0, está ordenado (caso base)
        return arr
    pivo = arr[0]
    menores = [i for i in arr[1:] if i <= pivo]
    maiores = [i for i in arr[1:] if i > pivo]
    #print('menores: ',menores)
    #print('maiores: ',maiores)
    return quickSort(menores) + [pivo] + quickSort(maiores)


print(quickSort([10,5,2,3]))