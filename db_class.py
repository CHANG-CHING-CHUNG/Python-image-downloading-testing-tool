import psycopg2 as pg2


class Database:
  def __init__(self, host, database, user, password):
    self.host = host
    self.database = database
    self.user = user
    self.password = password
    self.cur = None
    self.conn = None

  def connect(self):
    self.conn = pg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
    self.cur = self.conn.cursor()

  def execute_query(self, query,var):
    self.cur.execute(query,var)
    self.conn.commit()

  def close(self):
    self.cur.close()
    self.conn.close()

  def fetchone(self):
    return self.cur.fetchone()

  def fetchall(self):
    return self.cur.fetchall()

db = Database(
    host="localhost",
    database="img_test",
    user="postgres",
    password="postgres")

db.connect()