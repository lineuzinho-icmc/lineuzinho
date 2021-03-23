import psycopg2

class Connection():
    self.DATABASE_URL = os.environ['DATABASE_URL']
    def __init__(self):
        conn = psycopg2.connect(self.DATABASE_URL, sslmode='require')