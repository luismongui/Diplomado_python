from machine import Pin
from utime import sleep, sleep_ms
import network, time
from utelegram import Bot

TOKEN ='5799072520:AAFWvNGh9izlRou_krHKiTtQS8_Ik291yLo'
bot = Bot(TOKEN)

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
#Conectar a
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
def iniciar_proceso():
    if conectaWifi ("Xiaomi_2G", "12345678"):
        print ("Conexión exitosa!")
        print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
    else:
       print ("Imposible conectar")
       miRed.active (False) 
def message_using():
    @bot.add_message_handler('Hola')
    def help(update):
        update.reply('Hola como estas')
    bot.start_loop()
    
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
    iniciar_proceso()
    conexion = iniciar_proceso()
    if conexion ==True:
       message_using() 
    else:
       print("Fallos de red")     
        
    
    
    #lect = sensor.value()
   

