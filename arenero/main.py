from machine import Pin
from utime import sleep, sleep_ms

#Variables Globales
global estado_pir,estado_infl,contadorUso
estado_pir =0
estado_infl =0
contadorUso =0


#Lado Izquierdo
in1 = Pin(16, Pin.OUT)
in2 = Pin(17, Pin.OUT)
#Lado Derecho
in3 = Pin(5, Pin.OUT)
in4 = Pin(18, Pin.OUT)
#Sensor
rojo = Pin(22,Pin.OUT)
sensorPir = Pin(21,Pin.IN)
sensorInfl = Pin(19,Pin.IN)

def pasos(v1, v2, v3, v4):
    in1.value(v1)
    in2.value(v2)
    in3.value(v3)
    in4.value(v4)
    sleep_ms(10)
    
def contadorPir(num):
    num=num+1
    return num
def contadorInfl(num):
    num=num+1
    return num

def secuencia_dos_antirelog(cantidad):
  for i in range (cantidad):
    pasos(1,0,0,0)
    pasos(0,1,0,0)
    pasos(0,0,1,0)
    pasos(0,0,0,1)
    #print(i)
    
def secuencia_dos_relog(cantidad):
  for i in range (cantidad):
    pasos(1,1,0,0)
    pasos(0,1,1,0)
    pasos(0,0,1,1)
    pasos(1,0,0,1)
    #print(i)
    
def estado_sensor_pir():
    estado_pir = sensorPir.value()
    sleep(0.5)
    #print ("estado_pir",estado_pir)
    return estado_pir    
def estado_sensor_inflarojo():
    estado_infl = sensorInfl.value()
    sleep(0.5)
def enceder_led():
       rojo.value(1)
while True:
    #lect = sensor.value()
    secuencia_dos_relog(1)
    lecturaPir = estado_sensor_pir()
    lecturaInfl = estado_sensor_inflarojo()
    print("Est Pir:",lecturaPir,"Est Inf",lecturaInfl)
    if lecturaPir==1 :
        print("Gato en arenero....")
        enceder_led()
        secuencia_dos_relog(80)
    else:
     print("sin uso")

