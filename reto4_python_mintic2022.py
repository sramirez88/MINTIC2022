
def es_semestre_valido(p, s):

    dato=False
    semestre=1
    for i in range(len(p)):
        if semestre==s:
            dato=True
            break
        semestre+=1
    return dato

def es_semestre_vacio(p, s):

    dato=False
    if len(p[s-1])==0:
        dato=True
    return dato
def es_materia_valida(p, s, m):
    
    dato=False
    for i in range(len(p)):
        if i==s:
            if m in p[s-1]:
                dato=True
                break
    return dato

def modificar_materia(pensum, semestre, materia, nombre, creditos):
    
    if es_semestre_valido(pensum,semestre)==True:
        if es_semestre_vacio(pensum,semestre)==False:
            if  es_materia_valida(pensum, semestre, materia)==True:
                for i in pensum[semestre-1]:
                    if i==materia:
                        pensum[semestre-1][materia]={'nombre': nombre, 'créditos': creditos} 

def eliminar_materia(pensum, semestre, materia):

    if es_semestre_valido(pensum,semestre)==True:
        print('paso 1:ok')
        if es_semestre_vacio(pensum,semestre)==False:
            print('paso 2:ok')
            if  es_materia_valida(pensum, semestre, materia)==True:
                print('paso 3:ok')
                for i in pensum[semestre-1]:
                    if i==materia:
                        print('existe')
                        del pensum[semestre-1][materia]
                        print(pensum)
    
    
    
    # ESTA VEZ TU DEFINES TUS RETORNOS
