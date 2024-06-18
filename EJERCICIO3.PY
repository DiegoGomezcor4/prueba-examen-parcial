"""
EJERCICIOS 2) Se tiene los siguientes datos del nivel del rio (en metros) en el puerto de concordia, 
para los últimos 5 días hábiles de la semana. 
 
Escribir  un  programa  Python  para  permitir  ingresar  los  datos  por  consola  de  los  5  días  y 
guardarlos en una lista llamada altura_rio_puerto_concordia[]. 
a. Mostrar la altura mínima semanal y en qué día de la semana ocurrió. 
b. Mostrar la altura máxima semanal y en que día de la semana ocurrió. 
c. Calcular el promedio del nivel en la semana.
"""

#DATOS

fechas = ['5/6/2023','6/6/2023','7/6/2023','8/6/2023','9/6/2023']
alturas = [1.66, 1.88, 1.58, 2.08, 1.49]

#mostrar la altura minima

altura_minima = min(alturas)
dia_minimo = fechas[alturas.index(altura_minima)]
print(f'la altura minima semanal es {altura_minima}, y ocurrio el dia {dia_minimo}')