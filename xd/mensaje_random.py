from random import randint

mensajes = [
"jajaja es verdad",
"mira vos che",
"yo pienso lo mismo",
"esto con cristina no pasaba",
"al toke roque",
"al pike enrike",
 "Y es todo un tema",
 "mira las boludeces que escriben",
 "HOY SE COBRA"
]

class MensajeRandom(object):

    @staticmethod
    def fraseRandom():
        return mensajes[randint(0, len(mensajes)-1)]
