from sys import path
path.append('..\\modulos')
from machine import Pin
from utime import sleep, sleep_ms
import network, time, urequests
import _thread
from utelegram import Bot



TOKEN ='5530963040:AAE2WXhUzcULWyUHNsPpHwpE9FlLz8pv9pg'
bot = Bot(TOKEN) 
#Variables Globales
global estado_pir,estado_infl,contadorUso,manual,auto
estado_pir = 0
estado_infl = 0
contadorUso = 0
decremento =0
manual = 0
auto = 0
#Lado Izquierdo
in1 = Pin(16, Pin.OUT)
in2 = Pin(17, Pin.OUT)
#Lado Derecho
in3 = Pin(19, Pin.OUT)
in4 = Pin(18, Pin.OUT)
#Sensor
sensorPir = Pin(2,Pin.IN)
sensorInfl = Pin(21,Pin.IN)
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
          url ="https://maker.ifttt.com/trigger/deteccion_mascota/with/key/iCzsMo5HGaJhodkQmnr-RtbEPo3OUdXYLQRkQuCIRj2?"
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
    

#def message_using():
#    @bot.add_message_handler('Hola')
#    def help(update):
#        update.reply('''Hola Luis,Soy cathouse en que te puedo ayudar''')
#def message_usingArenero():
#    @bot.add_message_handler('arenero')
#    def help(update):
#        update.reply('''Arenero Inteligente \U0001F408,
#                        \n limpieza manual: manual
#                        \n limpieza automatica: auto
#                        \Gracias por usar nuestro protoipo''')#

#def message_using2():
#    @bot.add_message_handler('manual')
#    def help(update):
#        update.reply('Se inicia proceso manual')
#        manual=2
        
#def message_using3():
#    @bot.add_message_handler('auto')
#    def help(update):
#        update.reply('Limpieza automatico')
#        auto=3         
#    bot.start_loop()
  
def pasos(v1, v2, v3, v4):
    in1.value(v1)
    in2.value(v2)
    in3.value(v3)
    in4.value(v4)
    sleep(0.02)
    
def secuencia_una(cantidad):
  for i in range (cantidad):
    pasos(1,0,0,0)
    pasos(0,1,0,0)
    pasos(0,0,1,0)
    pasos(0,0,0,1)
    #print(i)
def secuencia_dos(cantidad):
  for i in range (cantidad):
    pasos(1,1,0,0)
    pasos(0,1,1,0)
    pasos(0,0,1,1)
    pasos(1,0,0,1)
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
def uso_telegram():
    url = "https://maker.ifttt.com/trigger/deteccion_mascota/with/key/iCzsMo5HGaJhodkQmnr-RtbEPo3OUdXYLQRkQuCIRj2?"
    respuesta = urequests.get(url+"&value1="+"200"+"&value2="+"Arenero Inteligente \U0001F408, El arenero esta en uso"+"&value3="+"Esperando para limpieza")
    print(respuesta.text)
    print(respuesta.status_code)
    respuesta.close ()
    
    
def limpieza_automatica():
     if manual==2:
         secuencia_una(10)
         print("Limpieando arenero manualmente")
     else:
        secuencia_una(10)
        print("Limpieando arenero manualmente")
#Este metodo permite utilizar un sensor pir para determinar si el arenero esta en uso      
def detecccion_mascota():
    lecturaPir = estado_sensor_pir()
    lecturaInfl = estado_sensor_inflarojo()
    print("Se encontro mascota con sensor Pir: ",lecturaPir)
    if lecturaInfl==0 and lecturaPir==1:
        contar_uso(1)
        uso_telegram()
    else:
        contar_uso(0)
        
#metodo de deteccion automatica         
def tarea_uno():
 while True:
    detecccion_mascota()
_thread.start_new_thread(tarea_uno,())
  
def contar_uso(n):
    global contadorUso
    while True:
        if n >= 1:
            contadorUso = contadorUso + 1
            print("Uso x segundo",contadorUso,n)
        else:
            break
        return contadorUso

def tarea_dos():
    global decremento
    for i in range(1,contadorUso):
         if contadorUso >= 6:
            limpieza_automatica() 
            decremento = contadorUso - 2 
         else:
            print("continuar deteccion automatica")
    
#metodo de limpieza automatica
while True:
    tarea_dos()
    #print("Conteo de uso:",contadorUso,"decremento;",decremento)

    
    
    
    