from datetime import datetime
from encodings import utf_8


def NoValido():
        fechaFormateada = datetime.now().strftime("%d/%m/%Y %H:%M")
        
        print("Se ingreso una opcion no valida")
        with open("log.txt", "a") as f:
                                                  f.write(f"{fechaFormateada} Se ingreso una opcion no valida\n")