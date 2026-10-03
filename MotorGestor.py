



from datetime import datetime
from encodings import utf_8











def TotalTareas (Tareas):
    
        fechaFormateada = datetime.now().strftime("%d/%m/%Y %H:%M")
        for Tarea in Tareas.values():
            print(Tarea)
        try:
              
              with open("log.txt", "a") as f:
                    f.write(f"{fechaFormateada} Se consultaron las tareas pendientes\n")  
        except OSError:
              with open("log.txt", "a") as f:
                    f.write(f"{fechaFormateada} No se logro la consulta\n")
        





                                                                    