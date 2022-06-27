
import numpy as np
import random

def encriptado(texto):

    comp=0
    cont=0
    lista=[]
    array_final=[]
    while comp**2<len(texto):
        comp+=1
    nuevo_mensaje=texto+(comp**2-len(texto))*"_"
    clave = np.arange(0,(comp*comp),1)
    random.shuffle(clave)
    for letra in nuevo_mensaje:
        lista.append(ord(letra))
    array_final = np.zeros((comp, comp))
    for i in range(comp):
        for j in range(comp):
            array_final[i][j]=lista[clave[cont]-1]
            cont+=1
    return array_final, clave


def desencriptado(array_encriptado, clave):

    original=array_encriptado.flatten().tolist()
    decodificado=[]
    texto=[]
    for i in range(len(clave)):
        original[i]=chr(int(original[i]))
    origen=original
    for i in original:
        decodificado.append(i)
    for i in range(len(clave)):
        decodificado[clave[i]] = original[i]
    texto = "".join(decodificado)  # convertir el array en string
    texto = texto.replace('_', '')
    return texto
