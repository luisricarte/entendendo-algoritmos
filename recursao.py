def regressiva(i):
    print(i)
    if i<=1: #caso base. (evita loop infinito)
        return
    else:
        regressiva(i-1) # uso de recursão
    
regressiva(12)