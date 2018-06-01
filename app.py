#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep
from random import randint
from xd.message_filter import *
from xd.mensaje_random import *
from random import randint
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
update_id = None

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

mensaje_random = MensajeRandom()
guerra = Guerra()
happy_filter = HappyFilter()
todo_filter = TodoFilter()
messi = Messi()
fresbe = Fresbe()
anda = AndaAlaCancha()
atiendo = Atiendo()
gil = Gil()
fat = Fat()
activa = Activa()
peron = Peron()
copa = Copaa()
sale = Salee()
bitcoin = Bitcoin()
menem = Menem()
choque = Choque()
bigdata = Bigdata()
jobs = Jobs()
merecer = Merece()
mirta = Mirta()
legrand = Legrand()
comoteven = Comoteven()
navidad = Navidad()
sosinimputable = Sosinimputable()
ort = Ort()
bot = Bot()
delarua = Delarua()
demo = Demo()
mama = Mama()
mate = Mate()
despegar = Despegar()
sofi = Sofi()
tom = Tom()
comer = Comer()
fact = Facturas()
bajar = Bajar()
chicas = Chicas()

def main():

    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("603336515:AAHFSGqGuYG6rJWtcQcLgMaheuxU5HVvTQw")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler(Filters.text, echo))
    
    dp.add_handler(MessageHandler(demo,demo1))
    dp.add_handler(MessageHandler(delarua,delarua1))
    dp.add_handler(MessageHandler(happy_filter,compro))
    dp.add_handler(MessageHandler(fresbe,pasameElFresbe1))
    dp.add_handler(MessageHandler(gil,gil1))
    dp.add_handler(MessageHandler(atiendo,atiendo1))
    dp.add_handler(MessageHandler(anda,anda1))
    dp.add_handler(MessageHandler(fat,fat1))
    dp.add_handler(MessageHandler(activa,activa1))
    dp.add_handler(MessageHandler(peron,peron1))
    dp.add_handler(MessageHandler(sale,sale1))
    dp.add_handler(MessageHandler(bitcoin,bitcoin1))
    dp.add_handler(MessageHandler(menem,menem1))
    dp.add_handler(MessageHandler(choque,choque1))
    dp.add_handler(MessageHandler(tom,tom1))
    dp.add_handler(MessageHandler(jobs,jobs1))
    dp.add_handler(MessageHandler(messi,messi1))
    dp.add_handler(MessageHandler(mate,mate1))
    dp.add_handler(MessageHandler(merecer,merecer1))
    dp.add_handler(MessageHandler(guerra,guerra1))
    dp.add_handler(MessageHandler(ort,ort1))  
    dp.add_handler(MessageHandler(mirta,mirta1))
    dp.add_handler(MessageHandler(legrand,legrand1))
    dp.add_handler(MessageHandler(comoteven,comoteven1))
    dp.add_handler(MessageHandler(sosinimputable,sosinimputabe1))
    dp.add_handler(MessageHandler(navidad,navidad1))
    dp.add_handler(MessageHandler(bigdata,bigdata1))
    dp.add_handler(MessageHandler(bot,bot1))
    dp.add_handler(MessageHandler(mama,mama1))
    dp.add_handler(MessageHandler(despegar,despegar1))
    dp.add_handler(MessageHandler(sofi,sofi1))
    dp.add_handler(MessageHandler(comer,comer1))
    dp.add_handler(MessageHandler(bajar,bajar1))
    dp.add_handler(MessageHandler(fact,fact1))
    dp.add_handler(MessageHandler(chicas,chicas1))
    dp.add_handler(MessageHandler(hotel,hotel1))
 
    """Este filter siempre tiene que estar ultimo"""
    dp.add_handler(MessageHandler(todo_filter, random))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()



def echo(bot,update):
    """Echo the user message."""
    logger.warning('Update "%s" caused error "%s"', update, 1)

def start(bot, update):
    update.message.reply_text('Adonde queres viajar??? ')
    
def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)
    

def chicas1(bot,update):
    chat_id = update.message.chat.id
    bot.sendPhoto(chat_id=update.message.chat.id, photo="https://images.larepublica.co/s3/280/cms/2017/02/06192652/Damian_scokin.jpg")

def hotel1(bot,update):
    chat_id = update.message.chat.id
    bot.send_message(chat_id=update.message.chat.id, ptext="TRIVAGO")

def tom1(bot,update):
    chat_id = update.message.chat.id
    bot.sendPhoto(chat_id=update.message.chat.id, photo="https://k61.kn3.net/0AE2053F9.jpg")
  
def comer1(bot,update):
    chat_id = update.message.chat.id
    bot.send_message(chat_id=update.message.chat.id, text="comete ESTAA")
      

def bajar1(bot,update):
    chat_id = update.message.chat.id
    bot.send_message(chat_id=update.message.chat.id, text="¿PUEDEN BAJAR LA MUSICA??")
    
def fact1(bot,update):
    chat_id = update.message.chat.id
    bot.send_message(chat_id=update.message.chat.id, text="FACTURAS")

def despegar1(bot,update):
    chat_id = update.message.chat.id
    bot.send_message(chat_id=update.message.chat.id, text="ALMUNDOOO")
    
def sofi1(bot,update):
    chat_id = update.message.chat.id
    bot.send_message(chat_id=update.message.chat.id, text="MATI TE AMOO!!!")
    
def mate1(bot,update):
    chat_id = update.message.chat.id
    bot.send_message(chat_id=update.message.chat.id, text="DAME UN MATE")
    
   
def delarua1(bot,update):
    chat_id = update.message.chat.id
    bot.send_message(chat_id=update.message.chat.id, text="Error 404 presidente not found")
    
def demo1(bot,update):
    chat_id = update.message.chat.id
    bot.send_message(chat_id=update.message.chat.id, text="Error 404 democracia not found")
    

def compro(bot,update):
    chat_id = update.message.chat.id
    bot.send_message(chat_id=update.message.chat.id, text="quiero llorar")

def pasameElFresbe1(bot,update):
    chat_id = update.message.chat.id
    bot.send_message(chat_id=update.message.chat.id, text="pasame el fresbeee")
    
def gil1(bot,update):
    chat_id = update.message.chat.id
    bot.send_message(chat_id=update.message.chat.id, text="sos boludo y no tenes huevos")
    
def fat1(bot,update):
    chat_id = update.message.chat.id
    bot.send_message(chat_id=update.message.chat.id, text="fat 32")

def mama1(bot,update):
    chat_id = update.message.chat.id
    bot.send_message(chat_id=update.message.chat.id, text="me contaste toda la loooooz")
    
def atiendo1(bot,update):
    chat_id = update.message.chat.id
    bot.send_message(chat_id=update.message.chat.id, text="atiendo bolu2")
    
def anda1(bot,update):
    chat_id = update.message.chat.id
    bot.send_message(chat_id=update.message.chat.id, text="anda a la cancha BOBO")
    
        
def activa1(bot,update):
    chat_id = update.message.chat.id
    bot.send_message(chat_id=update.message.chat.id, text="ACTIVA NEVER PONYY ")
    
    
def bitcoin1(bot,update):
    chat_id = update.message.chat.id
    bot.send_message(chat_id=update.message.chat.id, text="BITCONEEEECT")
    
    
def bigdata1(bot,update):
    chat_id = update.message.chat.id
    bot.sendPhoto(chat_id=update.message.chat.id, photo="https://amp.businessinsider.com/images/5acd1fe84d0386a9008b5052-750-500.jpg")
    
def menem1(bot,update):
    chat_id = update.message.chat.id
    bot.sendPhoto(chat_id=update.message.chat.id, photo="http://hdpnoticias.com.ar/wp-content/uploads/2016/02/Carlos-Menem-1.jpg")

def peron1(bot,update):
    chat_id = update.message.chat.id
    bot.send_message(chat_id=update.message.chat.id, text="LOS MUCHACHOS PERONISTAS TODOS UNI2 TRIUNFAREMOS....")
 
def choque1(bot,update):
	chat_id= update.message.chat.id
	bot.sendPhoto(chat_id=chat_id, photo='https://www.infobae.com/teleshow/infoshow/2017/08/18/absolvieron-a-chano-por-el-choque-en-belgrano-se-hizo-justicia/')
    
def sale1(bot,update):
	chat_id= update.message.chat.id
	bot.send_message(chat_id=update.message.chat.id, text="SALEE ")
    
def jobs1(bot,update):
	chat_id= update.message.chat.id
	bot.send_message(chat_id=update.message.chat.id, text="Apple = Humo")
	
def messi1(bot,update):
	chat_id= update.message.chat.id
	bot.send_message(chat_id=update.message.chat.id, text="Traeme la copa messi traeme la coopa")
	
def merecer1(bot,update):
	chat_id= update.message.chat.id
	bot.send_message(chat_id=update.message.chat.id, text="Porque messi SE LO MERESSI")
	
	
def mirta1(bot,update):
	chat_id= update.message.chat.id
	bot.send_message(chat_id=update.message.chat.id, text="mirtha legrand")
	
def legrand1(bot,update):
	chat_id= update.message.chat.id
	bot.send_message(chat_id=update.message.chat.id, text="dinosaurio")
	
def guerra1(bot,update):
	chat_id= update.message.chat.id
	bot.send_message(chat_id=update.message.chat.id, text="cualquier agujero es trinchera")
	
def comoteven1(bot,update):
	chat_id= update.message.chat.id
	bot.send_message(chat_id=update.message.chat.id, text="si te ven mal te maltratan y si te ven bien, te contratan")
	
def sosinimputabe1(bot,update):
	chat_id= update.message.chat.id
	bot.send_message(chat_id=update.message.chat.id, text="en 10 dias salis")
	
def navidad1(bot,update):
	chat_id= update.message.chat.id
	bot.send_message(chat_id=update.message.chat.id, text="Noo, porque mi familia eeee")
	
def programar1(bot,update):
	chat_id= update.message.chat.id
	bot.sendPhoto(chat_id=update.message.chat.id, photo="http://davidhayes.ca/wp-content/uploads/2016/10/Monkey-Typewriter-Simpsons.jpg")
	
def ort1(bot,update):
	chat_id= update.message.chat.id
	bot.sendPhoto(chat_id=update.message.chat.id, photo="https://i.ytimg.com/vi/ltvgaGFYsk8/maxresdefault.jpg")
	
def bot1(bot,update):
	chat_id= update.message.chat.id
	bot.send_message(chat_id=update.message.chat.id, text="mira las boludeces que escriben")


def random(bot,update):
	if randint(0,30)==1:
		chat_id= update.message.chat.id
		bot.send_message(chat_id=update.message.chat.id, text = mensaje_random.fraseRandom())


if __name__ == '__main__':
    main()
