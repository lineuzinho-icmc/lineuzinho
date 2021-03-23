from db import Connection
from random import randint
def pi(n):
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    for j in range(n):
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
        else:
            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2

def find_in_pi(pos):
    arr = ''
    #Generating pi to nTh digit
    for i in pi(10000):
        arr += str(i)
    return arr.find(str(pos))

def get_member_ranking(username):
    conn = Connection()
    member = conn.query_sql("SELECT * FROM members where username = '" + username + "'")
    ranked = sorted([(x[0], x[1], find_in_pi(x[2])) for x in conn.get_pi_members()], key=lambda tup: tup[2])
    if member:
        return str(ranked.index((member[0], member[1], find_in_pi(member[2]))) + 1) + "°: " + member[1] + ", respectiva posição nos dígitos de π: " + str(member[2]) + "\n"
    else:
        generate_member_ranking(username)
        member = conn.query_sql("SELECT * FROM members where username = '" + username + "'")
        ranked = sorted([(x[0], x[1], find_in_pi(x[2])) for x in conn.get_pi_members()], key=lambda tup: tup[2])
        return str(ranked.index((member[0], member[1], find_in_pi(member[2]))) + 1) + "°: " + member[1] + ", respectiva posição nos dígitos de π: " + str(member[2]) + "\n"
        

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
        msg += str(ranked.index(rank) + 1) + "°: " + rank[1] + ", respectiva posição nos dígitos de π: " + str(rank[2]) + "\n"
    return msg
    
def generate_daily_ranking():
    conn = Connection()
    for user in conn.get_usernames():
        generate_member_ranking(user)
    