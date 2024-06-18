"""
EJERCICIO 2) Para convertir entre las diferentes escalas de temperaturas Celsius (ºC), Fahrenheit 
(ºF) se realizan los siguientes cálculos: 
• De ºC a ºF: se multiplica por 1,8 y se suma 32. 
• De ºF a ºC: se resta 32 y se divide entre 1,8. 
Escribir un programa Python con dos funciones para permitir la conversión de escalas: 
convertir_celsius_fharenhait() 
convertir_fharenhait_celsius() 
2 
 
Mostrar la conversión de 53C° 
Mostrar la conversión de 77F° 
"""

def convertir_celsius_fharenhait(celsius):
    return celsius * 1.8 + 32


def convertir_fharenhait_celsius(fharenhait):
    return (fharenhait - 32) / 1.8

#Prueba de funcionamiento

# Conversion de 53°C a fharenheit

grados_celsius = 53
grados_fharenheit = convertir_celsius_fharenhait(grados_celsius)
print(f' {grados_celsius} grados celcius es igual a:  {grados_fharenheit} grados fharenheit')

# Conversion de 77° fharenheit

grados_fharenheit = 77
grados_celsius = convertir_fharenhait_celsius(77)
print(f'grados fharen: {grados_fharenheit}, grados celsius: {grados_celsius}')
