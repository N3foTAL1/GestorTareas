from datetime import datetime
from encodings import utf_8

def BienvSal():
      fechaFormateada = datetime.now().strftime("%d/%m/%Y %H:%M")
      try:
            print("Que deseas hacer hoy?\nVer las tareas pendientes Presiona 1\nRegistrar una nueva tarea Presiona 2\nVer historial de movimientos  Presiona 3\nSalir del programa Presiona 4 \n")
            
      finally:
            with open("log.txt", "a") as f:
                                            f.write(f"{fechaFormateada} Se inicio el programa\n")