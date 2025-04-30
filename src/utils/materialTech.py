import csv
from pathlib import Path

indice_v4 = "IV4"
indice_ixtot = "IX_TOT"

def clasificar_material(v4):
    """Clasifica el material de acuerdo al valor de v4"""
    if v4 in ['1', '2', '3', '4']:
        return "Material durable"
    elif v4 in ['5', '6', '7']:
        return "Material precario"
    elif v4 == '9':
        return "No aplica"
    else:
        return "Valor desconocido"

def clasificar_densidad(IX_TOT):
    """Clasifica la densidad de acuerdo al valor de IX_TOT"""
    valor = float(IX_TOT)
    if valor < 1:
        return "Bajo"
    elif valor < 2:
        return "Medio"
    else:  # valor >= 2
        return "Alto" 

def agregar_material_techumbre_y_densidad(archivo):
    """Agrega las columnas MATERIAL_TECHUMBRE y DENSIDAD HOGAR a un archivo CSV"""
    with open(archivo) as entrada:
        lector = csv.DictReader(entrada, delimiter=';')
        encabezado, cuerpo = next(lector), list(lector)

        # Le agregamos la nueva columna al encabezado
        nuevo_encabezado = encabezado + ['MATERIAL_TECHUMBRE', 'DENSIDAD HOGAR']

        with open(archivo, 'w', newline='') as salida:
            escritor = csv.DictReader(salida, delimiter=';')
            escritor.writerow(nuevo_encabezado)

            for fila in cuerpo:
                v4_valor = fila[indice_v4]
                ixtot_valor = fila[indice_ixtot]
                
                # Clasificar cada fila según el valor
                material = clasificar_material(v4_valor)
                densidad = clasificar_densidad(ixtot_valor)
                
                # Agregar las dos columnas nuevas
                fila.append(material)
                fila.append(densidad)
                escritor.writerow(fila)


