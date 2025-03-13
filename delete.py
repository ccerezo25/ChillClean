import os
import shutil
import ctypes
import winshell

# ruta donde se encuentra la carpeta de las descargas 
ruta_descargas = "C:\\Users\\servidor\\Downloads"
# ruta donde se encuentra mi carpeta de escanner 
ruta_escaner = "C:\\escaner"

def eliminar_contenido(carpeta):
    if os.path.exists(carpeta):
        for archivo in os.listdir(carpeta):
            ruta = os.path.join(carpeta, archivo)
            try:
                if os.path.isfile(ruta) or os.path.islink(ruta):
                    os.remove(ruta)  # Borra archivos
                elif os.path.isdir(ruta):
                    shutil.rmtree(ruta)  # Borra carpetas y su contenido
            except Exception as e:
                print(f"Error eliminando {ruta}: {e}")

def vaciar_papelera():
    try:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
        print("🗑 Papelera vaciada correctamente.")
    except Exception as e:
        print(f"Error al vaciar la papelera: {e}")

# Verifica si el script tiene permisos de administrador
if ctypes.windll.shell32.IsUserAnAdmin():
    print("Eliminando archivos de Descargas y Escaner...")
    eliminar_contenido(ruta_descargas)
    eliminar_contenido(ruta_escaner)

    print("Vaciando Papelera de Reciclaje...")
    vaciar_papelera()

    print("Eliminación completada con éxito.")
else:
    print("Debes ejecutar este script como administrador.")
