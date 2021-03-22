import random

class Greeter:
    def __init__(self):
        self.GREETINGS = [
            "roi {0} 😳👉👈 chama no pv",
            "vem co nois {0}! seja bem vinde!",
            "coe {0}, bien venidx ;)",
            "comequiceta {0}?? bem vinde!",
            "MEU DEUS OLHA QUEM CHEGO\nboas vindas {0} 🤤",
            "{0} ME NOTA EU SO SEU FÃ",
            "deem as boas vindas para a 8ª maravilha do mundo: {0}",
            "AGORA VAI\n{0} na área 🤩"
        ]

    def generateNewMembersGreetings(self, newMembers):
        welcomeVocative = ""
        if len(newMembers) > 1:
            for newMember in newMembers[:-1]:
                welcomeVocative += "{0}, ".format(newMember.first_name.split(" ")[0].lower())
            welcomeVocative += " e {0}".format(newMembers[-1].first_name.split(" ")[0].lower())
        else:
            welcomeVocative = newMembers[0].first_name.split(" ")[0].capitalize()
        
        rdWelcomeIndex = random.randint(0, len(self.GREETINGS) - 1)
        return self.GREETINGS[rdWelcomeIndex].format(welcomeVocative)