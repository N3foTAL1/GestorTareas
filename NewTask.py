from datetime import datetime
from encodings import utf_8

def NewTask ():
      fechaFormateada = datetime.now().strftime("%d/%m/%Y %H:%M")
      try:      
            NuevaFecha = datetime.now().strftime("%d/%m/%Y %H:%M")
            NuevaTarea = input("¿Cual es el Nombre de la nueva tarea?")
            NuevaImportancia = input("¿Cual es el nivel de importancia\nBajo Presiona 1\nMedio Presiona 2\nAlto Presiona 3\n")
            Importancia = int(NuevaImportancia)
            match (NuevaImportancia):
                                    case "1":
                                        Importancia = "Bajo"
                                    case "2":
                                        Importancia = "Medio"
                                    case "3":
                                        Importancia = "Alto"
                                    case _:
                                        print ("Opcion invalida")
            NuevoResponsable= input("Quien es el responsable")

            print(f"Se creo la siguiente tarea\n{NuevaFecha}\n{NuevaTarea}\n{Importancia}\n{NuevoResponsable}")
      finally:
                        with open("log.txt", "a") as f:
                                                  f.write(f"{fechaFormateada} Se agrego una nueva tarea\n") 