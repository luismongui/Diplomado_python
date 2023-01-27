from sys import path
path.append('..\\modulos')
from machine import Pin
from utime import sleep, sleep_ms
from utelegram import Bot
import _thread
import wifi_conect 
import messageTelegram
import limpieza
import connect


#Variables Globales
global estado_pir,estado_infl,contadorUso,manual,auto
estado_pir = 0
estado_infl = 0
contadorUso = 0
manual = 0
auto = 0
#Lado Izquierdo
in1 = Pin(16, Pin.OUT)
in2 = Pin(17, Pin.OUT)
#Lado Derecho
in3 = Pin(19, Pin.OUT)
in4 = Pin(18, Pin.OUT)
#Sensor
sensorPir = Pin(21,Pin.IN)
sensorInfl = Pin(2,Pin.IN)

#Conexion a wifi
connect.validacion_conexion("FamiliaM&M_router", "@S41rus3110")

messageTelegram.message_using()

limpieza.pasos(in1, in2, in3, in4)
    
def estado_sensor_pir():
    estado_pir = sensorPir.value()
    sleep(0.5)
    #print ("estado_pir",estado_pir)
    return estado_pir    
def estado_sensor_inflarojo():
    estado_infl = sensorInfl.value()
    sleep(0.5)
    return estado_infl

#Esta funcion permite que se pueda contar la cantidad de veces que se identifica un gato dentro de la arenera
def contar_uso(n):
    global contadorUso
    while True:
        if n >= 1:
            contadorUso = contadorUso + 1
            print("Uso x segundo",contadorUso,n)
        else:
            break
        return contadorUso

def limpieza_automatica():
     if manual==2:
         limpieza.secuencia_una(10)
         print("Limpieando arenero manualmente")
     else:
        limpieza.secuencia_una(10)
        print("Limpieando arenero automatico")
      
def detecccion_mascota():
    lecturaPir = estado_sensor_pir()
    lecturaInfl = estado_sensor_inflarojo()
    print("Se encontro mascosta: ",lecturaPir)
    messageTelegram.message_using("probando mensaje")
    if lecturaInfl==0 and lecturaPir==1:
        contar_uso(1)
        print("Gato en arenero....",contadorUso)
    else:
        contar_uso(0)
        messageTelegram.message_using("El arenero no esta en uso: ")
        print("sin uso el arenero")
_thread.start_new_thread(detecccion_mascota(), ())

while True:
    messageTelegram.message_using("usando prototipo automatico")
    if contadorUso>=6  :
        limpieza_automatica()
        contadorUso = 0
    else:
        print("continuar deteccion")