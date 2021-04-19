import os

from internal.greeter import Greeter
from internal.forwarder import Forwarder
from internal.pi_ranker import PiRanker
from internal.beaner import Beaner
from internal.ainer import Ainer

from internal.activityAgiota import ActivityAgiota

class Lineuzinho:

    def __init__(self):
        self.API_TOKEN = os.environ["SECRET"]
        self.contatinhosSheet = "http://bit.ly/contatosbcc021"
        self.githubRepo = "https://github.com/lineuzinho-icmc/lineuzinho"
        self.subjectsGroupsLinks = "\nICC1: https://t.me/joinchat/cxOk_L889nc2NDk5\n\nMONITORIA ICC1: https://t.me/joinchat/xYXv3oiuMP8xYzA5\n\nLAB ICC1 [Tarde]: https://t.me/joinchat/4KTLgPVis483NDUx\n\nLAB ICC1 [Noite]: https://t.me/joinchat/23qmmmmAnCg1ZDQx\n\nEletrônica: https://t.me/joinchat/0oBPQIAN17kwZTNh\n\nCálculo 1: https://t.me/joinchat/loEfiwcvAV82ZmVh\n\nGA: https://t.me/joinchat/3i-Kuf256mo1ODA5\n\nILD: https://t.me/joinchat/TItjZehheg44NjIx\n\nPLD https://t.me/joinchat/ClHA1xPsSBRjZWUx\n\nAVISOS: https://t.me/joinchat/B5qbuFd8x483ZThh"
        self.usefulLinks = "Se achar algum bixo de BCC021 que não tá aqui passa o link!\nbit.ly/grupobcc021\n\nGuia do Bixo: https://bit.ly/3c9mcUG\n\nEnquetes: https://t.me/joinchat/qrJ_MrnHDbE1ZmNh\n\nJogos: https://t.me/joinchat/wNjNYOmK96ozMmYx\n\nDrives dos livros:\nhttp://bit.ly/livrosbccicmc\nICC I: https://drive.google.com/file/d/1oafsU0c8v1NqQ4ALDpLSC785cmTwMubU/view?usp=sharing\n\n"
        self.docsChannel = "https://t.me/docs21"

        self.greeter = Greeter()
        self.forwarder = Forwarder()
        self.piRanker = PiRanker()
        self.ainer = Ainer()
        self.beaner = Beaner()

        self.activityAgiota = ActivityAgiota()

    def start(self, update, context):
        update.message.reply_text("pó fala meu rei")

    def greet(self, update, context):
        newMembers = update.message.new_chat_members
        greetings = self.greeter.generateNewMembersGreetings(newMembers)
        context.bot.send_message(chat_id=update.effective_chat.id, text=greetings)

    def getGeneralRelevantLinks(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=self.usefulLinks, disable_web_page_preview=True)
        
    def getLivesLinks(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=self.lives, disable_web_page_preview=True)

    def getSubjectsGroupsLinks(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=self.subjectsGroupsLinks, disable_web_page_preview=True)

    def getRepo(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=self.githubRepo)

    def getContatinhosLink(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="CHAMA NOS CONTATINHO\n{0}".format(self.contatinhosSheet), disable_web_page_preview=True)

    def getDocsChannel(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=self.docsChannel)

    def saveMessage(self, update, context):
        self.forwarder.saveToDocs(update, context)

    def getBeanFlavor(self, update, context):
        beanFlavor = self.beaner.getFlavor()
        context.bot.send_message(chat_id=update.effective_chat.id, text=beanFlavor)

    def getPiRanking(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=self.piRanker.getDailyRanking())

    def publishUserPiRanking(self, update, context):
        username = update.message.from_user.username
        self.piRanker.generateUserPiRank(update.message.from_user.username)
        context.bot.send_message(chat_id=update.effective_chat.id, text=self.piRanker.getUserPiRank(username))

    def getHelpText(self, update, context):
        update.message.reply_text("digita \"/\" no teclado pra dar uma olhada nos comandos disponíveis :V")

    def getRandomAin(self, update, context):
        ainPath = self.ainer.getRandomAinPath()
        context.bot.send_audio(chat_id=update.effective_chat.id, audio=open(ainPath, 'rb'))
    
    def getBirthdaySongAudio(self, update, context):
        context.bot.send_audio(chat_id=update.effective_chat.id, audio=open('resources/birthday.mp3', 'rb'))

    def getBeniSongAudio(self, update, context):
            context.bot.send_audio(chat_id=update.effective_chat.id, audio=open('resources/beni.mp3', 'rb'))

    def agiotar(self, update, context):
        self.activityAgiota.randomAnnoy(update)