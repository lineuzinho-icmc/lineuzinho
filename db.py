import os, psycopg2

class Connection():
    DATABASE_URL = os.environ['DATABASE_URL']

    def execute_sql(self, sql):
        conn = psycopg2.connect(self.DATABASE_URL, sslmode='require')
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()

    def query_sql(self, sql):
        conn = psycopg2.connect(self.DATABASE_URL, sslmode='require')
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result

    def get_members(self):
        conn = psycopg2.connect(self.DATABASE_URL, sslmode='require')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM members")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    def get_usernames(self):
        conn = psycopg2.connect(self.DATABASE_URL, sslmode='require')
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM members")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return [x[0] for x in result]

    def get_pi_members(self):
        conn = psycopg2.connect(self.DATABASE_URL, sslmode='require')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM members WHERE pi_rank IS NOT NULL")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result