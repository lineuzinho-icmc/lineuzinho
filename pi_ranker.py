from random import randint
import json, datetime, math_pi

class PiRanker:
    def __init__(self):
        self.pi = math_pi.pi()
        self.preProcPiRanks = json.load(open('resources/pi-score_pre-proc.json'))
        self.piCall = datetime.datetime.now().date()
        self.piRanks = {}

    def getPiDecimalPosition(self, pos):
        return self.preProcPiRanks[str(pos)]

    def getUserPiRank(self, username):
        return "{0}: seu pi-rank diário é {0} PI".format(username, self.piRanks[username])

    def generateUserPiRank(self, username):
        self.checkRankExpiration()
        if not username in self.piRanks.keys():
            self.piRanks[username] = self.getPiDecimalPosition(randint(0, 999))

    def getDailyRanking(self):
        self.checkRankExpiration()
        if not self.piRanks:
            return "como e que ce quer ranking se ninguem gerou index ainda?"

        usersRanking = sorted(self.piRanks, key=self.piRanks.get, reverse=False)
        rankingReport = 'PiRanking fresquinho pro ces familia'
        for index, username in enumerate(usersRanking):
            rankingReport += "\n{0}° {1} - {2} PI".format(index+1, username, self.piRanks[username])
        return rankingReport

    def checkRankExpiration(self):
        if datetime.datetime.now().date() > self.piCall:
            self.piRanks = {}
            self.piCall = datetime.datetime.now().date()