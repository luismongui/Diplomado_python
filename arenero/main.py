from machine import Pin
from utime import sleep, sleep_ms
import network, time
from utelegram import Bot

TOKEN ='5530963040:AAE2WXhUzcULWyUHNsPpHwpE9FlLz8pv9pg'
bot = Bot(TOKEN) 

#Variables Globales
global estado_pir,estado_infl,contadorUso
estado_pir = 0
estado_infl = 0
contadorUso = 0
#Lado Izquierdo
in1 = Pin(16, Pin.OUT)
in2 = Pin(17, Pin.OUT)
#Lado Derecho
in3 = Pin(5, Pin.OUT)
in4 = Pin(18, Pin.OUT)
#Sensor
rojo = Pin(19,Pin.OUT)
sensorPir = Pin(21,Pin.IN)
sensorInfl = Pin(2,Pin.IN)
#Conectar a
#Conexion a wifi
def conectaWifi (red, password):
      global miRed
      miRed = network.WLAN(network.STA_IF)     
      if not miRed.isconnected():              #Si no está conectado…
          miRed.active(True)                   #activa la interface
          miRed.connect(red, password)         #Intenta conectar con la red
          print('Conectando a la red', red +"…")
          timeout = time.time ()
          while not miRed.isconnected():           #Mientras no se conecte..
              if (time.ticks_diff (time.time (), timeout) > 10):
                  return False
      return True
#Funcion para validar la conexion de red
def validacion_conexion(red,clave):
    if conectaWifi (red, clave):
        print ("Conexión exitosa!")
        print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
    else:
           print ("Imposible conectar")
           miRed.active (False)
    

       
def message_using(message):
    @bot.add_message_handler('Hola')
    def help(update):
        update.reply('Hola Luis,'+ message)

def message_using2():
    @bot.add_message_handler('manual')
    def help(update):
        update.reply('Limpieza manual')
        
def message_using3():
    @bot.add_message_handler('automatico')
    def help(update):
        update.reply('Limpieza automatoca')
          
    bot.start_loop()
  
def pasos(v1, v2, v3, v4):
    in1.value(v1)
    in2.value(v2)
    in3.value(v3)
    in4.value(v4)
    sleep_ms(15)

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
    #sleep_ms(10)
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
    
validacion_conexion("FamiliaM&M_router", "@S41rus3110")

def limpieza_automatica():
    if contadorUso>=3:
       #secuencia_dos_relog(60)
       print("Limpieando arenero")
       contadorUso =0
    else:
       print("El Arenero sigue en uso")

    
        
def detecccion_mascota():
    lecturaPir = estado_sensor_pir()
    lecturaInfl = estado_sensor_inflarojo()
    print("Est Pir:",lecturaPir,"Est Inf",lecturaInfl)
    if lecturaInfl==0 and lecturaPir==1:
        contar_uso(1)
        print("Gato en arenero....",contadorUso)
    else:
        contar_uso(0)
        message_using("El arenero no esta en uso: ")
        print("sin uso el arenero")
while True:
    global contadorUso
    detecccion_mascota()
    if contadorUso>=100  :
        limpieza_automatica
        print("realizando  limpieza")
        contadorUso = 0
    else:
        print("continuar deteccion")

