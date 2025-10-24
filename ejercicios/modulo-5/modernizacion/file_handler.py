# ej-m5-modernizacion/file_handler.py
import os
from pathlib import Path

def get_report_path_legacy(report_name: str, user: str) -> str:
    """
    Construye la ruta a un archivo de reporte usando la librería 'os' (estilo antiguo).
    """
    
    # Obtener el home del usuario de forma compatible
    home_dir = os.path.expanduser("~")
    
    # Construir la ruta usando os.path.join (verboso y propenso a errores)
    reports_dir = os.path.join(home_dir, "Documents", "Reports", user)
    
    # Asegurarse de que el directorio existe
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)
        
    file_path = os.path.join(reports_dir, report_name)
    
    print(f"Ruta de reporte (legacy): {file_path}")
    return file_path

# 1. Importar 'Path' de 'pathlib'.
# 2. Crear una nueva función 'get_report_path_modern' que haga lo mismo que la anterior.
# 3. Usar Tabnine para ayudar a reescribirla con los operadores '/' de pathlib.
def get_report_path_modern(report_name: str, user: str) -> str:
    """
    Construye la ruta a un archivo de reporte usando la librería 'pathlib'.
    """
    
    # Obtener el home del usuario de forma compatible
    home_dir = Path.home()
    
    # Construir la ruta usando Path.join (verboso y propenso a errores)
    reports_dir = home_dir / "Documents" / "Reports" / user
    
# 4. Usar '.mkdir(parents=True, exist_ok=True)' para crear el directorio.
    reports_dir.mkdir(parents=True, exist_ok=True)
        
    file_path = reports_dir / report_name
    
    print(f"Ruta de reporte (modern): {file_path}")
    return str(file_path)

