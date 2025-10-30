# ej-m5-modernizacion/file_handler.py
import os

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

# --- Misión del Alumno ---
# 1. Importar 'Path' de 'pathlib'.
# 2. Crear una nueva función 'get_report_path_modern' que haga lo mismo.
# 3. Usar Tabnine para ayudar a reescribirla con los operadores '/' de pathlib.
#    (Ej: Path.home() / "Documents" / "Reports" / user)
# 4. Usar '.mkdir(parents=True, exist_ok=True)' para crear el directorio.