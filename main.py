"""Este gestrer de tareas tiene la finalidd de llevar un registro diario de tareas pendientes
para tener una trazabilidad en tiempo y tearas de los pendientes y su nivel de prioridad"""



# Se importa el modulo datetime para manejar las fechas
from ast import Import, match_case
from multiprocessing import Value
from pickle import TRUE
import trace

import Historial
import MotorGestor
import datetime

import NoValido
import Bienvenida
import Historial
import NewTask
import Salir





Tareas = {
    "Fecha":datetime.date(2026, 9, 8),
    "NomTarea": "Tomar Clase de Programacion",
    "Importancia": "Critica",
    "Responsable":"Dan Lara",
    "Fecha01": datetime.date(2026, 9, 9),
    "NomTarea01": "Hacer tarea de Lenguas",
    "Importancia01": "Critica",
    "Responsable01":"Dan Lara",
    "Fecha02":datetime.date(2026, 9, 16),
    "NomTarea02": "Ir al cine",
    "Importancia02": "Normal",
    "Responsable02":"Dan Lara"
}








while True:
    Bienvenida.BienvSal()
    Gestor_Tareas = input("Elije una opcion \n")

    match Gestor_Tareas:
                case "1":
                    MotorGestor.TotalTareas(Tareas)
                               
                case "2":
                    NewTask.NewTask()
                case "3":
                    Historial.historial()
                case "4":
                    Salir.Salir()
                    break
                
                case _:
                    NoValido.NoValido()

if __name__ == "__main__"
    main()
                     
                
            



        
        


