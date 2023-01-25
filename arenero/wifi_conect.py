import network, time

class Connect():
    #Clase para connectarse a internet
    red = Connect()
    password = Connect()
    
    def __init__(self, red,password):
        self.red = red
        self.password = password
    
    def conectaWifi (self,red, password):
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
    def validacion_conexion(self,red,clave):
        if conectaWifi (red, clave):
            print ("Conexión exitosa!")
            print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
        else:
               print ("Imposible conectar")
               miRed.active (False)
        return miRed
