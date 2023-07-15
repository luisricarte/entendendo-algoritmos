#exercício 4.1
def recursao2(array,soma=0):
    if len(array) == 0:
        return print(soma)
    soma = soma + array[0]
    array.pop(0)
    recursao2(array,soma)


recursao2([1,2,3,4])