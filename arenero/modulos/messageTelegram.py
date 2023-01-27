
from utelegram import Bot

class messageTelegram:
 
 TOKEN ='5530963040:AAE2WXhUzcULWyUHNsPpHwpE9FlLz8pv9pg'
bot = Bot(TOKEN) 
         
def message_using():
    @bot.add_message_handler('arenero')
    def help(update):
        update.reply('''Hola Luis,Soy cathouse en que te puedo ayudar,
                        \n Arenero Inteligente \U0001F408
                        \n limpieza manual: manual
                        \n limpieza automatica: auto
                        \Gracias por usar nuestro protoipo''')

def message_using2():
    @bot.add_message_handler('manual')
    def help(update):
        update.reply('Se inicia proceso manual')
        manual=2
        
def message_using3():
    @bot.add_message_handler('auto')
    def help(update):
        update.reply('Limpieza automatico')
        auto=3
          
    bot.start_loop()