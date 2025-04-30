
import csv
def noNacidosArg(año , trimestre, archivo):
    """informa porcentaje de personas no argentinas y hayan cursado un nivel universitario o sup"""

        #CH12 nivel mas alto cursado 7 univeristario , 8 y 9 superior y CH13 si finalizo (1 si, 2 no)
        #CH15  4. En un país limítrofe (especi car:Brasil, Bolivia, Chile, Paraguay,Uruguay)5. En otro país (especi car)9. Ns/Nr
    index_pondera = 9
    index_ch12 = 19
    index_ch13 = 20
    index_ch15 = 22
    index_año = 1
    index_trimestre = 2
    with open(archivo) as file :
        csv_reader = csv.reader(file, delimiter=";")
        next(csv_reader) # Salto la primera fila (encabezado)

        # Inicializo contadores
        totalPersonas = 0
        totalNoArg = 0
        for line in csv_reader:

            if(line[index_año] == str(año)) and (line[index_trimestre] == str(trimestre)):
               # Mostrar el valor de pondera antes de convertirlo
                print(f"Pondera antes de convertir: {line[index_pondera]}")  # Aquí estamos viendo el valor original
                
                try:
                    pondera = float(line[index_pondera].strip())  # Convertir pondera a float
                except ValueError:
                    print(f"Error al convertir Pondera: {line[index_pondera]}")  # Imprimir si hay error
                    pondera = 0  # Si no se puede convertir, asignar 0
                totalPersonas += pondera
                # Verificar las condiciones de personas no nacidas en Argentina y que hayan cursado un nivel universitario o superior
                print(f"CH15: {line[index_ch15]}, CH12: {line[index_ch12]}, CH13: {line[index_ch13]}")
                if (line[index_ch15]) > "3" and (line[index_ch12] > "6") and (line[index_ch13] == "1"):
                    print(f"INCLUIDO - CH15: {index_ch15}, CH12: {index_ch12}, CH13: {index_ch13}, PONDERA: {pondera}")
                    totalNoArg += pondera 

    if totalNoArg == 0:
        print("ninguna cuenta cumple con los requisitos")
    else:
        print(f"Total de personas no argentinas que han cursado un nivel universitario o superior: {totalNoArg}")
        print(f"Total de personas: {totalPersonas}")
    try:
        porcentaje = (totalNoArg / totalPersonas) * 100
        return porcentaje
    except ZeroDivisionError:
        print("Error: no se puede dividir por cero.")
        return 0 


def obtener_anos_trimestres(archivo):
    """Extrae los años y trimestres únicos del archivo"""
    anos_trimestres = set()  # Usamos un set para evitar duplicados
    with open(archivo) as file:
        csv_reader = csv.reader(file, delimiter=";")
        next(csv_reader)  # Saltamos la primera fila (encabezado)

        # Recorremos el archivo y extraemos los años y trimestres
        for line in csv_reader:
            año = line[1] 
            trimestre = line[2]  
            anos_trimestres.add((año, trimestre))  # Agregamos como tupla para tener ambos valores

    return sorted(anos_trimestres)  # Devolvemos la lista de años y trimestres ordenados





