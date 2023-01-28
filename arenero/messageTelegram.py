import time, urequests

def uso_telegramEntrada():
        respuesta = urequests.get(url+"&value1="+"200"+"&value2="+"Arenero Inteligente \U0001F408, El arenero esta en uso"+"&value3="+"Esperando para limpieza")
        print(respuesta.text)
        print(respuesta.status_code)
        return respuesta.close ()
def uso_telegramSalida():
        respuesta = urequests.get(url+"&value1="+"200"+"&value2="+"Arenero Inteligente \U0001F408, El arenero esta en uso"+"&value3="+"Limpieza finalizada")
        print(respuesta.text)
        print(respuesta.status_code)
        return respuesta.close ()


if __name__==("__main__"):
        print(__name__)
        uso_telegramEntrada()
else:
        print(__name__)
        pritn("practica modulo")
        