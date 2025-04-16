from src.cant_casas import cant_casas

def porcentaje_propietarios(datos):
    cant_prop = 0
    for renglon in datos:
        if renglon[37] == '1':
            cant_prop += int(renglon[8])
    casas = cant_casas(datos)
    return (cant_prop / casas) * 100