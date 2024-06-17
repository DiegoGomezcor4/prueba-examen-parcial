"""
) Escribir un programa Python que calcule el índice de masa corporal de una persona 
(IMC).  
 
Muestre por pantalla el estado en el que se encuentra esa persona en función del valor de IMC: 
Valor de IMC | Diagnóstico 
< 16 | Criterio de ingreso en hospital 
De 16 a 17 | Infrapeso 
De 17 a 18 | Bajo peso 
De 18 a 25 | Peso normal (saludable) 
De 25 a 30 | Sobrepeso (obesidad de grado I) 
De 30 a 35 | Sobrepeso crónico (obesidad de grado II) 
De 35 a 40 | Obesidad premórbida (obesidad de grado III) 
> 40 | Obesidad mórbida (obesidad de grado IV) 
"""


def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def diagnostico_imc(imc):
    if imc < 16:
        return 'Criterio de ingreso en hospital'
    elif 16 <= imc < 17:
        return 'Infrapeso'
    elif 17 <= imc < 18:
        return 'Bajo peso'
    elif 18 <= imc < 25:
        return 'Peso normal (saludable)'
    elif 25 <= imc < 30:
        return 'Sobrepeso (Obesidad de gradoI)'
    elif 30 <= imc < 35:
        return 'Sobrepeso cronico (Obesidad de grado II)'
    elif 35 <= imc < 40:
        return 'Obesidad premorbida (obesidad de grado III)'
    else:
        return 'Obesidad morbida (obesidad de grado IV)'
    

def main():
    try:
        peso = float(input('Intruduce tu peso en kiglogramos: '))
        altura = float(input('Intruduce tu altura en metros: '))

        imc = calcular_imc(peso, altura)
        diagnostico = diagnostico_imc(imc)

        print(f'Tu IMC es: {imc:.2f}')
        print(f'Diagnóstico: {diagnostico}')
    except ValueError:
        print('Por favor, introduce valores numericos validos para peso y altura')


if __name__ == '__main__':
    main()
    

    