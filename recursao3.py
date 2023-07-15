#exercício 4.2
def recursao3(arr,valor):
    if len(arr) == 0:
        return print(valor)
    valor += 1
    arr.pop(0)
    recursao3(arr,valor)

recursao3([1,2,3,4,5],0)