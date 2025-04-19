def cant_casas(cuerpo):
    cant = 0
    for renglon in cuerpo:
        cant += int(renglon[8])
    return cant