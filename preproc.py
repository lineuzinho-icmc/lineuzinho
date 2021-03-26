import math_pi
import json

ranks = {}
pi = str(math_pi.pi())[2:]

for i in range(1000):
    rank = pi.find(str(i))
    ranks[i] = rank

with open('pi-score_pre-proc.json', 'w') as fp:
    json.dump(ranks, fp)