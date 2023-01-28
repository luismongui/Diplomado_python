import network, time
from machine import Pin
from utelegram import Bot

TOKEN ='5799072520:AAFWvNGh9izlRou_krHKiTtQS8_Ik291yLo'
bot = Bot(TOKEN)



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


if conectaWifi ("Xiaomi_2G", "12345678"):

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
    
    @bot.add_message_handler('Hola')
    def help(update):
        update.reply('El sistema esta validando el uso')
    bot.start_loop()
 
else:
       print ("Imposible conectar")
       miRed.active (False)
