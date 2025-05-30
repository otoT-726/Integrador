from pathlib import Path
from src.utils.rutas import data_path
def correspondencias():
    """Devuelve una lista de archivos sin correspondencia y qué tipo falta (hogar o individuo)."""
    lista_archivos_actuales = [archivo.name for archivo in data_path.iterdir() if archivo.name.startswith("usu")]
    
    codigos = {}
    for archivo in lista_archivos_actuales:
        partes = archivo.split("_")
        tipo = partes[1]  # hogar o indi...
        codigo = partes[2].split(".")[0]  # T123, T223, etc.
        
        if codigo not in codigos:
            codigos[codigo] = set()
        codigos[codigo].add(tipo)

    sin_correspondencia = []
    for codigo, tipos in codigos.items():
        if "hogar" not in tipos:
            sin_correspondencia.append((f"usu_individual_{codigo}.txt", "falta hogar"))
        elif "individual" not in tipos and "indi" not in tipos:  # por si se llama 'usu_indi'
            sin_correspondencia.append((f"usu_hogar_{codigo}.txt", "falta individuo"))

    return sin_correspondencia
