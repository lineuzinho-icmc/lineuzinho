import logging
import random
import constant

class Lineuzinho:
    def __init__(self):
        self.greetings = [
            "roi {0} 😳👉👈 chama no pv",
            "vem co nois {0}! seja bem vinde!",
            "coe {0}, bien venidx ;)",
            "comequiceta {0}?? bem vinde!",
            "MEU DEUS OLHA QUEM CHEGO\nboas vindas {0} 🤤",
            "{0} ME NOTA EU SO SEU FÃ",
            "deem as boas vindas para a 8ª maravilha do mundo: {0}",
            "AGORA VAI\n{0} na área 🤩"
        ]

        self.usefulLinks = "Estamos adicionando todo mundo aos poucos. Se puder ajudar a achar o pessoal, passa o link do grupo na descrição!\n\nInscrição na semana de recepção: calouros.icmc.usp.br/\n\nGuia do Bixo: https://bit.ly/3c9mcUG\n\nContatinho de geral: {0}\n\n".format(constant.CONTATINHOS_SHEET)

    def start(self, update, context):
        update.message.reply_text("pó fala meu rei")

    def getContatinhos(self, update, context):
        update.message.reply_text("CHAMA NOS CONTATINHO\n{0}".format(constant.CONTATINHOS_SHEET), disable_web_page_preview=True)

    def greet(self, update, context):
        newMembers = update.message.new_chat_members
        welcomeVocative = ""
        if len(newMembers) > 1:
            for newMember in newMembers[:-1]:
                welcomeVocative += "{0}, ".format(newMember.first_name.split(" ")[0].lower())
            welcomeVocative += " e {0}".format(newMembers[-1].first_name.split(" ")[0].lower())
        else:
            welcomeVocative = newMembers[0].first_name.split(" ")[0].capitalize()
        
        rdWelcomeIndex = random.randint(0, len(self.greetings) - 1)
        update.message.reply_text(self.greetings[rdWelcomeIndex].format(welcomeVocative))

    def links(self, update, context):
        update.message.reply_text(self.usefulLinks, disable_web_page_preview=True)    

    def getRepo(self, update, context):
        update.message.reply_text(constant.GITHUB_REPO)

    def help(self, update, context):
        update.message.reply_text("digita \"/\" no teclado pra dar uma olhada nos comandos disponíveis :V")

    def save(self, update, context):
        originalMessage = update.message.reply_to_message
        if not originalMessage:
            update.message.reply_text("faz o comando respondendo alguma coisa...")

        context.bot.forwardMessage("@docs21", update.effective_chat.id, originalMessage.message_id)

    def getDocsChannel(self, update, context):
        update.message.reply_text(constant.DOCS_CHANNEL)
