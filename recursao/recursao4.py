#exercicio 4.3
def encontra_maior(arr,menor=99999999999999999):
    if len(arr)== 0:
        return print(menor)
    if menor >= arr[0]:
        menor = arr[0]
    arr.pop(0)
    encontra_maior(arr,menor)

encontra_maior([3,2,5,1.1,1])