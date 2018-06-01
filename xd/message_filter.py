#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import BaseFilter

class Bajar(BaseFilter):
	def filter(self,message):
		return "http://youtu.be/" in message.text.lower() or "youtube" in message.text.lower()
		
class Chicas(BaseFilter):
	def filter(self,message):
		return "chica" in message.text.lower() or "rrhh" in message.text.lower() or "jefe" in message.text.lower()
			
class Facturas(BaseFilter):
	def filter(self,message):
		return "rompi" in message.text.lower() or "cague" in message.text.lower() or "cagué" in message.text.lower() or "rompí" in message.text.lower() or "flashe" in message.text.lower() or "jira" in message.text.lower() or "lucio" in message.text.lower()

class Programar(BaseFilter):
	def filter(self, message):
		return "developer" in message.text.lower() or "despegar" in message.text.lower() or "accenture" in message.text.lower() or  " mono 	y" in message.text.lower() or ("program" in message.text.lower() and "codigo" in message.text.lower() ) or  ("comput" in message.text.lower() and "program" in message.text.lower() ) or "programador" in message.text.lower() or "developer" in message.text.lower()

class Bigdata(BaseFilter):
	def filter(self, message):
		return "big data" in message.text.lower() or  ("dato" in message.text.lower() and "vende" in message.text.lower() ) or  ("info" in message.text.lower() and "vende" in message.text.lower() )

class Demo(BaseFilter):
    def filter(self, message):
        return "venezuela" in message.text.lower() or "cuba" in message.text.lower() or "stanlin" in message.text.lower()  or "elecciones" in message.text.lower()
      
class Delarua(BaseFilter):
    def filter(self, message):
        return "delarua" in message.text.lower() or "de la rua" in message.text.lower()
        
class Sofi(BaseFilter):
    def filter(self, message):
        return "sofi " in message.text.lower() or " sofi" in message.text.lower()
        
class Comer(BaseFilter):
	def filter(self, message):
		return "hambre" in message.text.lower() or "comer" in message.text.lower() or "comemos" in message.text.lower() or "alimentar" in message.text.lower()

class Michetti(BaseFilter):
    def filter(self, message):
        return "michetti" in message.text.lower()

class Tom(BaseFilter):
    def filter(self, message):
        return "tomar" in message.text.lower() or  "bullrich" in message.text.lower() or "escabi" in message.text.lower() or "birra" in message.text.lower() or "vino" in message.text.lower() or "ferne" in message.text.lower()

class Mate(BaseFilter):
    def filter(self, message):
        return "mate" in message.text.lower() or "mate" in message.text.lower()
        
class Despegar(BaseFilter):
    def filter(self, message):
        return "despegar" in message.text.lower()
        
class Mama(BaseFilter):
    def filter(self, message):
        return "mama" in message.text.lower() or ( "se corto" in message.text.lower() and "luz" in message.text.lower()) or "ricky" in message.text.lower() or "cortaste" in message.text.lower()

class Bot(BaseFilter):
    def filter(self, message):
        return " bot " in message.text.lower() or "robot" in message.text.lower() or " bots " in message.text.lower() or  "morseador" in message.text.lower() or "morsa" in message.text.lower() or "matias m" in message.text.lower()

class Salee(BaseFilter):
    def filter(self, message):
        return "sale" in message.text.lower() or "dalee" in message.text.lower() or  "vama" in message.text.lower() or "vamo" in message.text.lower() or "vamos" in message.text.lower()


class Facho(BaseFilter):
	def filter(self, message): 
		return "hay que matarlo" in message.text.lower() or "facho" in message.text.lower() or "hay que matarlos" in message.text.lower() or "choriplaneros" in message.text.lower()

class Fresbe(BaseFilter):
    def filter(self, message):
        return "pasame" in message.text.lower() or "fresbe" in message.text.lower() or "frisbi" in message.text.lower() 
 
class Ort(BaseFilter):
    def filter(self, message):
        return ("ort" in message.text.lower() and "institucion" in message.text.lower())or ("ort" in message.text.lower() and "secundaria" in message.text.lower()) or ("ort" in message.text.lower() and "publica" in message.text.lower()) or ("ort" in message.text.lower() and "colegio" in message.text.lower()) or ("ort" in message.text.lower() and "estudi" in message.text.lower()) or " TIC " in message.text.lower() or "ort montañeses" in message.text.lower() or "ort yatay" in message.text.lower() or "ministerio de educacion" in message.text.lower()  or " colegio " in message.text.lower() or ( "educacion" in message.text.lower()  and "publica"  in message.text.lower()) or ( "sitema" in message.text.lower()  and "educ"  in message.text.lower())
       
class Merece(BaseFilter):
    def filter(self, message):
        return "messi" in message.text.lower() or "futbol argentino" in message.text.lower() 
        
class Messi(BaseFilter):
    def filter(self, message):
        return "mundial" in message.text.lower() or "futbol" in message.text.lower()
        
        
class Choque(BaseFilter):
    def filter(self, message):
        return " choque " in message.text.lower() or " chano " in message.text.lower() or " chocar " in message.text.lower() or " manejar " in message.text.lower() or " choco " in message.text.lower()


class HappyFilter(BaseFilter):
    def filter(self, message):
        return "radiohead" in message.text.lower() or "macri" in message.text.lower()
        
 
class DejarGobernar(BaseFilter):
    def filter(self, message):
        return "vidal" in message.text.lower() or "macri" in message.text.lower() or "bullrich" in message.text.lower()

class Bitcoin(BaseFilter):
    def filter(self, message):
        return "bitcoin" in message.text.lower() or "blockchain " in message.text.lower() or "satoshi" in message.text.lower() or "bitconect" in message.text.lower()
     
        
class Peron(BaseFilter):
    def filter(self, message):
        return "peron" in message.text.lower() or "cristina" in message.text.lower() or "marcha" in message.text.lower() or ("cortar" in message.text.lower() and "9 de julio" in message.text.lower()) or ("cortar" in message.text.lower() and "calle" in message.text.lower()) or ("cortar" in message.text.lower() and "avenida" in message.text.lower())
  
class Copaa(BaseFilter):
    def filter(self, message):
        return "dsahudsadisadsadsai" in message.text.lower()
        
class AndaAlaCancha(BaseFilter):
    def filter(self, message):
        return "partido" in message.text.lower() or "cancha" in message.text.lower()
        
class Sosinimputable(BaseFilter):
    def filter(self, message):
        return "sos inimputable" in message.text.lower()	
        
class Navidad(BaseFilter):
	def filter(self,message):
		return "navidad" in message.text.lower() and "simon" in message.text.lower()
        
class Guerra(BaseFilter):
    def filter(self, message):
        return "en epocas de guerra" in message.text.lower() or " guerra " in message.text.lower() or "en epoca de guerra" in message.text.lower() or "en tiempos de guerra" in message.text.lower()

class Fat(BaseFilter):
    def filter(self, message):
        return "fiesta" in message.text.lower() or " box " in message.text.lower() or " jodita " in message.text.lower() or " fat " in message.text.lower()

class Menem(BaseFilter):
    def filter(self, message):
        return "2000" in message.text.lower() or "forro" in message.text.lower()  or "menem" in message.text.lower() or "carlos" in message.text.lower() or "saul" in message.text.lower() or "2001" in message.text.lower()
  

class Atiendo(BaseFilter):
    def filter(self, message):
        return "atiendo" in message.text.lower() or "boludos" in message.text.lower()
        
class Gil(BaseFilter):
    def filter(self, message):
        return "bobo" in message.text.lower() or "tonto" in message.text.lower() or " gil " in message.text.lower() or "gordo" in message.text.lower()
        
class Jobs(BaseFilter):
	def filter(self,message):
		return "steve" in message.text.lower() or " jobs " in message.text.lower() or " apple " in message.text.lower() or "iphone" in message.text.lower() or " ipod " in message.text.lower() or " ios " in message.text.lower() or " mac " in message.text.lower()

class Activa(BaseFilter):
    def filter(self, message):
        return "coger" in message.text.lower() or "wacha" in message.text.lower()  or "garchar" in message.text.lower() or "ponerla" in message.text.lower()
    
class Mirta(BaseFilter):
	def filter(self,message):
		return "vieja chota" in message.text.lower() or "dinosarurio"  in message.text.lower()

class Legrand(BaseFilter):
	def filter(self,message):
		return "mirta" in message.text.lower() or "mirtha" in message.text.lower() or "legrand" in message.text.lower()
		
class Comoteven(BaseFilter):
	def filter(self,message):
		return "como te ven" in message.text.lower()
		
class Relativo(BaseFilter):
	def filter(self,message):
		return "relativo" in message.text.lower() or "einstein" in message.text.lower() or "fisica " in message.text.lower()

class Hotel(BaseFilter):
	def filter(self, message):
		return "hotel" in message.text.lower()

class TodoFilter(BaseFilter):
    def filter(self, message):
        return message.text != ""

