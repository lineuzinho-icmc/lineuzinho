from random import choice

class Greeter:
    def __init__(self):
        self.greetings = [
            "roi {0} π³ππ chama no pv",
            "vem co nois {0}! seja bem vinde!",
            "coe {0}, bien venidx ;)",
            "comequiceta {0}?? bem vinde!",
            "MEU DEUS OLHA QUEM CHEGO\nboas vindas {0} π€©",
            "{0} ME NOTA EU SO SEU FΓ π³ππ",
            "EIS A 8Βͺ MARAVILHA DO MUNDO: {0} π€€",
            "AGORA VAI\n{0} na Γ‘rea π€©"
        ]

    def generateNewMembersGreetings(self, newMembers):
        welcomeVocative = newMembers[0].first_name.split(" ")[0]
        greeting = choice(self.greetings)

        if self.greetings.index(greeting) < 4:
            return greeting.format(welcomeVocative.capitalize())
        else:
            return greeting.format(welcomeVocative.upper())