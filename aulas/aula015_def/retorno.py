import os


os.system('cls')
# metro = distancia / 100
# km = distancia / 1000
# minutos = tempo / 00.60
# horas = tempo / 60.00
# Definindo a função
def calcular_velocidade_media(distancia, tempo):
    # Vm = ΔS/ΔT
    velocidade_media = distancia / tempo
    metro = distancia / 100
    km = distancia / 1000
    minutos = tempo / 00.60
    horas = tempo / 01.00
    
    return velocidade_media



distancia = float(input('Digite a distancia percorrida: '))
tempo = float(input('Digite o tempo gasto : '))



# Calcular a velocidade media usando função criada
velocidade_m = calcular_velocidade_media(distancia, tempo)
velocidade_km = calcular_velocidade_media(distancia, tempo)

# Exibir o resultado
print(f'A velocidade media é {velocidade_km:.2f} km/h')
print(f'A velocidade media em metro é {velocidade_m:.2f} m')
