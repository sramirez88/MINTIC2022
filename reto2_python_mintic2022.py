# POR FAVOR LEA TODAS LAS INDICACIONES SUMINISTRADAS EN EL 
# ENUNCIADO ANTES DE EMPEZAR A IMPLEMENTAR SU SOLUCIÓN
pensum = [
{'0123': {'nombre': 'intro a la ing', 'créditos': 2},
'4567': {'nombre': 'inglés', 'créditos': 1}},
{}, {}
]

# NO MODIFICAR EL NOMBRE, PARÁMETROS O RETORNO DE LA FUNCIÓN
def modificar_materia(pensum, semestre, materia, nombre, creditos):
    while semestre<4 and semestre>=1:
        if len(pensum[semestre-1])==0:
            mensaje="El semestre no tiene materias"
            break
        else:
            break
    if (semestre-1)<0 or (semestre-1)>=3:
        mensaje="Ingrese un semestre válido"
  
    while semestre==1:
        if materia in pensum[0]:
            pensum[0][materia]={'nombre': nombre, 'créditos': creditos}
            mensaje="Modificada con éxito"
            break
        if materia not in pensum[0]:
            mensaje="La materia no existe"
            break
    # ACÁ INICIA LA FUNCIÓN modificar_materia (En este espacio debes 
    # poner el código necesario para implementar esta funcionalidad)
    # ACÁ TERMINA LA FUNCIÓN modificar_materia
    # NO MODIFIQUES LA SIGUIENTE LÍNEA
    return mensaje

