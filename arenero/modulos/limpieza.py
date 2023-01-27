from utime import sleep, sleep_ms

class limpieza:
   
  def __init__ (self,v1,v2,v3,v4,cantidad):
    self.v1 = v1
    self.v2 = v2
    self.v3 = v3
    self.v4 = v4
    self.cantidad = cantidad
 
  def pasos (self):
      in1.value(self.v1)
      in2.value(self.v2)
      in3.value(self.v3)
      in4.value(self.v4)
      sleep(0.02)
      
  def secuencia_una(self):
    for i in range (self.cantidad):
      pasos(1,0,0,0)
      pasos(0,1,0,0)
      pasos(0,0,1,0)
      pasos(0,0,0,1)

  def secuencia_dos(self):
    for i in range (self.cantidad):
      pasos(1,1,0,0)
      pasos(0,1,1,0)
      pasos(0,0,1,1)
      pasos(1,0,0,1)
      
  def secuencia_dos_relog(self):
    for i in range (self.cantidad):
      pasos(1,1,0,0)
      pasos(0,1,1,0)
      pasos(0,0,1,1)
      pasos(1,0,0,1)
     