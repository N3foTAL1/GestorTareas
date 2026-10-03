from datetime import datetime
from encodings import utf_8

def historial():
      try:
        with open("log.txt","r", encoding="utf_8") as f:
            print (f.read()) 
            f.close()     
      except FileNotFoundError:
              print("No se encontro el archivo de log")