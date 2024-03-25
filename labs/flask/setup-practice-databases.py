import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# kirlinp is superuser
# check if practice db exists, if not, create it
conn = psycopg2.connect(host="dbclass.rhodescs.org", user="kirlinp", password="kirlinp", dbname="postgres")
cur = conn.cursor()

cur.execute("select * from pg_database where datname='practice'")
result = cur.fetchone()
if not result: # database doesn't exist
  conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
  cur = conn.cursor()
  cur.execute("CREATE DATABASE practice;")
  print("Creating practice database.")
else:
  print("Practice database already exists, skipping.")

# re-login

conn = psycopg2.connect(host="dbclass.rhodescs.org", user="kirlinp", password="kirlinp", dbname="practice")
cur = conn.cursor()

logins = ["sample"]
file = open("logins2.txt")
logins = [line.strip() for line in file.readlines()]

for username in logins:
  username_quoted = '"' + username + '"'
  print("Doing " + username)
        
  cur.execute("DROP SCHEMA IF EXISTS \"" + username + "\" CASCADE;")
  cur.execute("CREATE SCHEMA AUTHORIZATION \"" + username + "\";")
  cur.execute("GRANT ALL PRIVILEGES ON SCHEMA \"" + username + "\" TO \"" + username + "\";");

conn.commit()

cur.close()
conn.close()

