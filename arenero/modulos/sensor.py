from utime import sleep, sleep_ms


class sensor:
    def estado_sensor_pir(sensorPir):
        estado_pir = sensorPir.value()
        sleep(0.5)
        #print ("estado_pir",estado_pir)
        return estado_pir    
    def estado_sensor_inflarojo(sensorInfl):
        estado_infl = sensorInfl.value()
        sleep(0.5)
        return estado_infl