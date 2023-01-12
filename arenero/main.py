from machine import Pin
from utime import sleep,sleep_ms

rojo = Pin(19,Pin.OUT)
sensor = Pin(18,Pin.IN)
global numero
numero = 0

def contador(num):
    num=num+1
    return num

def prueba():
    lectura= sensor.value()
    print(lectura)
    sleep(0.5)
    numero + 1

    if lectura==1:
        rojo.value(1)
    else:
        rojo.value(0)
while True:
    prueba()
    
