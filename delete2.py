import os
import shutil
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


eliminar_contenido(ruta_descargas)
eliminar_contenido(ruta_escaner)
vaciar_papelera()
print("Eliminación completada con éxito.")
