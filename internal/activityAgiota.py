from random import randint, choice

class ActivityAgiota:
    def __init__(self):
        self.cobradas = [
            "Oi, {0}, desculpa atrapalhar, mas... ce já fez suas atividades de hoje? 😳👉👈",
            "Faça atividade imediatamente ou serás banido do grupo 😠😤",
            "tá falano pacaralho no grupo e fazer trampo que é bom nada né",
            "hahah pdp pdp e as atividades lá, tão pronta já? ",
            "s-s-senpai-chan 😳, já fizeste v-vossas atividades?",
            "MLQ VAI FICA NO TELEGRAM DIA INTEIRO?\nFAZ FACULDADE NAO??",
            "viu, quantos crédito ce ta fazendo falando no telegram?",
            "pelo amor de deus {0} arruma essa postura",
            "já se hidratou hoje??? levanta e vai tomar uma água!",
            "a escoliose vem, hein? senta direito meu chapa"   
        ]

    def randomAnnoy(self, update):
        username = update.message.from_user.username
        if randint(0, 300) == 250:
            update.message.reply_text(choice(self.cobradas).format(username))
