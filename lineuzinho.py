import logging
import random
import os

from greeter import Greeter
from forwarder import Forwarder

class Lineuzinho:
    def __init__(self):
        self.API_TOKEN = os.environ["SECRET"]
        self.CONTATINHOS_SHEET = "https://shorturl.at/nMOV2"
        self.GITHUB_REPO = "https://github.com/lineuzinho-icmc/lineuzinho"
        self.USEFUL_LINKS = "Estamos adicionando todo mundo aos poucos. Se puder ajudar a achar o pessoal, passa o link do grupo na descrição!\n\nInscrição na semana de recepção: calouros.icmc.usp.br/\n\nGuia do Bixo: https://bit.ly/3c9mcUG\n\nContatinho de geral: {0}\n\n".format(self.CONTATINHOS_SHEET)
        self.DOCS_CHANNEL = "https://t.me/docs21"

        self.greeter = Greeter()
        self.forwarder = Forwarder()

    def start(self, update, context):
        update.message.reply_text("pó fala meu rei")

    def getContatinhos(self, update, context):
        update.message.reply_text("CHAMA NOS CONTATINHO\n{0}".format(self.CONTATINHOS_SHEET), disable_web_page_preview=True)

    def greet(self, update, context):
        newMembers = update.message.new_chat_members
        greetings = self.greeter.generateNewMembersGreetings(newMembers)
        update.message.reply_text(greetings)

    def links(self, update, context):
        update.message.reply_text(self.USEFUL_LINKS, disable_web_page_preview=True)    

    def getRepo(self, update, context):
        update.message.reply_text(self.GITHUB_REPO)

    def help(self, update, context):
        update.message.reply_text("digita \"/\" no teclado pra dar uma olhada nos comandos disponíveis :V")

    def save(self, update, context):
        self.forwarder.saveToDocs(update, context)

    def getDocsChannel(self, update, context):
        update.message.reply_text(self.DOCS_CHANNEL)

    