import csv

def calcular_porcentaje(archivo_individuos):
    #Inputs para ingresar aglomerados
    aglomeradoA = input("Ingrese el primer Aglomerado")
    aglomeradoB = input("Ingrese el segundo Aglomerado") 
    
    print("Aglomerado A: ", aglomeradoA)
    print("Aglomerado B: ", aglomeradoB)
    
    anoActual = ""
    trimActual = ""
    dic_por_ano_trimestre = {}
    # Abrimos el archivo de hogares
    with open(archivo_individuos) as ah:
        csv_dict_reader = csv.DictReader(ah)
        for fila in csv_dict_reader:
            ano = fila["ANO4"]          
            trim = fila["TRIMESTRE"]    
            pondera = fila["PONDERA"]   
            aglomerado = fila["AGLOMERADO"]
            edad = int(fila["CH06"])
            nivel_educativo = int(fila["CH12"])
            
            ano_trim = (ano, trim)
            #aca guardo una tupla con el ano y el trimestre para ponerlas
            #como clave del diccionario
            
            if aglomeradoA == aglomerado or aglomeradoB == aglomerado:
                if ano_trim not in dic_por_ano_trimestre:
                    dic_por_ano_trimestre[ano_trim] = {
                        "A":{"mayores": 0, "secundario_incompleto": 0},
                        "B":{"mayores": 0, "secundario_incompleto": 0}
                    }
                
                grupo = "A" if aglomerado == aglomeradoA else "B"
                
                if edad >= 18:
                    dic_por_ano_trimestre[grupo]["mayores"] += pondera
                    
                    if(nivel_educativo<4):
                        dic_por_ano_trimestre[grupo]["secundario_incompleto"] += pondera
        
        #busco una forma linda de impresion.
        
        print("\n{:<6} {:<10} {:<15} {:<15}".format("ANO", "TRIMESTRE", "AGLOMERADO A", "AGLOMERADO B"))
        
        for clave in sorted(dic_por_ano_trimestre.keys()):
            ano,trim = clave
            mayoresA = dic_por_ano_trimestre[clave]["A"]["mayores"]
            sec_incompleto_a = dic_por_ano_trimestre[clave]["A"]["secudario_incompleto"]

            mayoresB = dic_por_ano_trimestre[clave]["B"]["mayores"]
            sec_incompleto_b = dic_por_ano_trimestre[clave]["B"]["secundario_incompleto"]
            
            porcentaje_a = (sec_incompleto_a / mayoresA * 100) if mayoresA != 0 else 0
            porcentaje_b = (sec_incompleto_b / mayoresB * 100) if mayoresB != 0 else 0
           
            print("{<6} {:<10} {:<15} {:<15}".format(ano,
                                                     trim,
                                                     f"{porcentaje_a:.0f}%",
                                                     f"{porcentaje_b:.0f}%"
                                                     ))