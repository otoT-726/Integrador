from pathlib import Path



project_path = Path(__file__).parent.parent.parent #Path a la carpeta global del trabajo

data_path = project_path / "archivos" #Path a la carpeta de archivos


print(data_path)