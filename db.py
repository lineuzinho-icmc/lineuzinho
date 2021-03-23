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

    def get_members(self):
        conn = psycopg2.connect(self.DATABASE_URL, sslmode='require')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM members")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result