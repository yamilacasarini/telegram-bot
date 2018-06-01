from random import randint

mensajes = [
"jajaja es verdad",
"mira vos che",
"yo pienso lo mismo",
"esto con cristina no pasaba",
"al toke roque",
"al pike enrike",
 "por?",
 "es al pedo empujar cuando la pija es muy corta",
 "Algo de eso hay",
 "Y es todo un tema",
 "STAY WERE YOU ARE",
 "TAG YOUR LOCAL DRUG DEALER",
 "¿Cuando sale un asadito?",
 "diculpame flacx podes hablar en un lenguajx mas inclusivx"
]

class MensajeRandom(object):

    @staticmethod
    def fraseRandom():
        return mensajes[randint(0, len(mensajes)-1)]
