votaram = {}

def verificaVoto(nome):
    if votaram.get(nome):
        return print("Has voted!")
    votaram[nome] = True
    return print("Can vote!")


verificaVoto("duds")
verificaVoto("duds")