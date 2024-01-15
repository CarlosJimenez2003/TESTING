def funcio1(num: int)->int:
    #codi de la funció funcio1#
    resultat = 0

    if(num>0):
        resultat = 1 #Si "num" es mes gran que 0 retorna 1
    elif(num==0):
        resultat = 0 #Si "num" es igual a 0 retorna 0
    else:
        resultat = -1 #Si "num" no es ni un ni el altre retorna -1
    
    return resultat