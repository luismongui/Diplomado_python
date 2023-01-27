import network, time, urequests
from dht import DHT11
from machine import Pin

led = Pin(2, Pin.OUT)

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

sensorDHT = DHT11(Pin(15))

if conectaWifi ("WILPEC", "73397340"):

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
      
    url = "https://maker.ifttt.com/trigger/sensortemp/with/key/b8a4iyhDEK5Rfvlx12CtD7?"  
    
    while True:
        time.sleep(4)
        sensorDHT.measure()
        temp=sensorDHT.temperature()
        hum=sensorDHT.humidity()

        print ("T={:02d} ºC, H={:02d} %".format(temp,hum))
        
        if temp > 20:
            
            respuesta = urequests.get(url+"&value1="+str(temp)+"&value2="+str(hum))
            print(respuesta.text)
            print(respuesta.status_code)
            respuesta.close ()
            led.value(1)
            
        else:
            led.value(0)
        
 
else:
       print ("Imposible conectar")
       miRed.active (False)