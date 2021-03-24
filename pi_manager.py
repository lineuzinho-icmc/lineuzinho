from db import Connection
from random import randint
def pi():
    pi = ''
    with open('pi.txt', 'r') as filename:
        pi = filename.read()
    return pi

def find_in_pi(pos):
    arr = ''
    #Generating pi to nTh digit
    for i in pi():
        arr += str(i)
    return arr.find(str(pos))

def get_member_ranking(username):
    conn = Connection()
    member = conn.query_sql("SELECT * FROM members where username = '" + username + "'")
    ranked = sorted([(x[0], x[1], find_in_pi(x[2])) for x in conn.get_pi_members()], key=lambda tup: tup[2])
    if member:
        return str(ranked.index((member[0], member[1], find_in_pi(member[2]))) + 1) + "°: " + member[1] + ", posição em π: " + str(member[2]) + "\n"
    else:
        generate_member_ranking(username)
        member = conn.query_sql("SELECT * FROM members where username = '" + username + "'")
        ranked = sorted([(x[0], x[1], find_in_pi(x[2])) for x in conn.get_pi_members()], key=lambda tup: tup[2])
        return str(ranked.index((member[0], member[1], find_in_pi(member[2]))) + 1) + "°: " + member[1] + ", posição em π: " + str(member[2]) + "\n"
        

def generate_member_ranking(username):
    conn = Connection()
    #Verify if user is already in db
    if [i for i, v in enumerate(conn.get_members()) if v[1] == username]:
        num = str(randint(0, 1000))
        while find_in_pi(num) == -1:
            num = str(randint(0, 1000))

        conn.execute_sql("UPDATE members SET pi_rank = " + str(num) + " WHERE username = '" + username + "'")
    else:
        num = str(randint(0, 1000))
        while find_in_pi(num) == -1:
            num = str(randint(0, 1000))
        conn.execute_sql("INSERT INTO members (username, pi_rank) VALUES ('" + username + "', " + num + ");")

def get_daily_ranking():
    conn = Connection()
    msg = ''
    ranked = sorted([(x[0], x[1], find_in_pi(x[2])) for x in conn.get_pi_members()], key=lambda tup: tup[2])
    for rank in ranked:
        msg += str(ranked.index(rank) + 1) + "°: " + rank[1] + ", posição em π: " + str(rank[2]) + "\n"
    return msg
    
def generate_daily_ranking():
    conn = Connection()
    for user in conn.get_usernames():
        generate_member_ranking(user)
    