import os

from internal.greeter import Greeter
from internal.beaner import Beaner
from internal.forwarder import Forwarder
from internal.activityAgiota import ActivityAgiota
from internal.pi_ranker import PiRanker
import datetime
import time, random

class Lineuzinho:

    def __init__(self):
        self.API_TOKEN = os.environ["SECRET"]
        self.contatinhosSheet = "http://bit.ly/contatosbcc021"
        self.githubRepo = "https://github.com/lineuzinho-icmc/lineuzinho"
        self.lives = "Live da primeira semana: http://bit.ly/aberturadasemana \n\nLive do JB: bit.ly/calldojb\n\n"
        self.usefulLinks = "Estamos adicionando todo mundo aos poucos. Se puder ajudar a achar o pessoal, passa o link do grupo na descrição!\n\nInscrição na semana de recepção: calouros.icmc.usp.br/\n\nGuia do Bixo: https://bit.ly/3c9mcUG\n\nContatinho de geral: {0}\n\nEnquetes: https://t.me/joinchat/qrJ_MrnHDbE1ZmNh\n\nDrive com livros: http://bit.ly/livrosbccicmc\n\n".format(self.contatinhosSheet)
        self.docsChannel = "https://t.me/docs21"

        self.greeter = Greeter()
        self.forwarder = Forwarder()
        self.beaner = Beaner()
        self.activityAgiota = ActivityAgiota()

        self.piRanker = PiRanker()

    def start(self, update, context):
        update.message.reply_text("pó fala meu rei")

    def greet(self, update, context):
        newMembers = update.message.new_chat_members
        greetings = self.greeter.generateNewMembersGreetings(newMembers)
        context.bot.send_message(chat_id=update.effective_chat.id, text=greetings)

    def links(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=self.usefulLinks, disable_web_page_preview=True)

    def getRepo(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=self.githubRepo)

    def getContatinhos(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="CHAMA NOS CONTATINHO\n{0}".format(self.contatinhosSheet), disable_web_page_preview=True)

    def getDocsChannel(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=self.docsChannel)

    def save(self, update, context):
        self.forwarder.saveToDocs(update, context)

    def getBeanFlavor(self, update, context):
        beanFlavor = self.beaner.getFlavor()
        context.bot.send_message(chat_id=update.effective_chat.id, text=beanFlavor)

    def getPiRanking(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=self.piRanker.getDailyRanking())

    def generateUserPiRanking(self, update, context):
        username = update.message.from_user.username
        self.piRanker.generateUserPiRank(update.message.from_user.username)
        context.bot.send_message(chat_id=update.effective_chat.id, text=self.piRanker.getUserPiRank(username))

    def help(self, update, context):
        update.message.reply_text("digita \"/\" no teclado pra dar uma olhada nos comandos disponíveis :V")

    def agiotar(self, update, context):
        self.activityAgiota.randomAnnoy(update)
    
    def birthday(self, update, context):
        context.bot.send_audio(chat_id=update.effective_chat.id, audio=open('resources/birthday.mp3', 'rb'))
