import serial
from time import sleep

arduino=serial.Serial('COM7',9600)#NOME DO SERIAL DO ARDUINO E SUA PORTA DEFINIDA, NA MAIORIA DAS VZS O PADRÃO É COM3 MSM

def ligar_led(led_num):
    arduino.write(str(led_num).encode())
def desligar_led(led_num):
    arduino.write(str(led_num).encode())
def ligar_todos():
    arduino.write('A'.encode())
def desligar_todos():
    arduino.write('D'.encode())
    
def sequencia1(time):
    for _ in range(5):
        for i in range(1,6):
            ligar_led(i)
            sleep(0.5)
            desligar_led(i)

        for i in range(5,0,-1):
            ligar_led(i)
            sleep(0.5)
            desligar_led(i)
        sleep(time)
        desligar_todos()

try:
    while True:
        print("1-ACENDER LED 1")
        print("2-ACENDER LED 2")
        print("3-ACENDER LED 3")
        print("4-ACENDER LED 4")
        print("5-ACENDER LED 5")
        print("Z-ACENDER TODOS OS LEDS")
        print("K-APAGAR TODOS OS LEDS")
        print("X-INICIAR SEQUÊNCIA")
        pergunta=input("COLOQUE O QUE DESEJA FAZER: ").upper()
         
        if pergunta=='Z':
            ligar_todos()
        elif pergunta=='K':
            desligar_todos()
        elif pergunta=='X':
            time=int(input("COLOQUE QUANTO TEMPO QUER QUE A SEQUÊNCIA DURE: "))
            sequencia1(time)
        elif pergunta in ['1','2','3','4','5']:
            ligar_led(int(pergunta))
        else:
            print("COLOQUE ALGO VÁLIDO")
except KeyboardInterrupt:
    print("PROGRAMA FOI INTERROMPIDO")
    desligar_todos()
    arduino.close()