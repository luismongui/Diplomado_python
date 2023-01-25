from utime import sleep, sleep_ms


def estado_sensor_pir():
    estado_pir = sensorPir.value()
    sleep(0.5)
    return estado_pir    
def estado_sensor_inflarojo():
    estado_infl = sensorInfl.value()
    sleep(0.5)
    return estado_infl


