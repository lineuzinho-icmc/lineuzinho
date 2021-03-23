import os, pi_manager

from db import Connection
from greeter import Greeter
from forwarder import Forwarder
from beaner import Beaner
import time, random

class Lineuzinho:

    def __init__(self):
        self.API_TOKEN = os.environ["SECRET"]
        self.contatinhosSheet = "http://bit.ly/contatosbcc021"
        self.githubRepo = "https://github.com/lineuzinho-icmc/lineuzinho"
        self.usefulLinks = "Estamos adicionando todo mundo aos poucos. Se puder ajudar a achar o pessoal, passa o link do grupo na descrição!\n\nInscrição na semana de recepção: calouros.icmc.usp.br/\n\nGuia do Bixo: https://bit.ly/3c9mcUG\n\nContatinho de geral: {0}\n\nEnquetes: https://t.me/joinchat/qrJ_MrnHDbE1ZmNh\n\n".format(self.contatinhosSheet)
        self.docsChannel = "https://t.me/docs21"

        self.greeter = Greeter()
        self.forwarder = Forwarder()
        self.beaner = Beaner()

        self.conn = Connection()
        self.last_pi_call = time.time()

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
        if time.time() - self.last_pi_call > 86400:
            self.last_pi_call = time.time()
            pi_manager.generate_daily_ranking()
        context.bot.send_message(chat_id=update.effective_chat.id, text=pi_manager.get_daily_ranking())

    def getUserPiRanking(self, update, context):
        if time.time() - self.last_pi_call > 86400:
            self.last_pi_call = time.time()
            pi_manager.generate_daily_ranking()
        context.bot.send_message(chat_id=update.effective_chat.id, text=pi_manager.get_member_ranking(update.message.from_user.username))

    def help(self, update, context):
        update.message.reply_text("digita \"/\" no teclado pra dar uma olhada nos comandos disponíveis :V")

    def randomActivityAlert(self, update, context):
        if random.randint(0, 500) == 250:
            update.message.reply_text("Oi, desculpa atrapalhar, mas... já fez suas atividades de hoje? :)")
            
    def rojao(self, update, context):
        numeroDePra = random.randint(1,4)
        numeroDePow = random.randint(0,3)

        update.message.reply_text("bora acender essa porra")
        update.message.reply_text("pra pra pra")

        for x in range(0, numeroDePra):
            update.message.reply_text("pra")

        update.message.reply_text("pra pra")

        for x in range(0, numeroDePow):
            update.message.reply_text("POOOOWW")
