from datetime import datetime
from encodings import utf_8


def Salir ():
  
        fechaFormateada = datetime.now().strftime("%d/%m/%Y %H:%M")
        print("Saliendo del Programa ...... programa cerrado")
        with open("log.txt", "a") as f:
                                                      f.write(f"{fechaFormateada} El usuario cerro el programa\n")

