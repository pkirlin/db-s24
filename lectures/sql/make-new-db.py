# add schemas (pg "schemas") for each user in the logins file for a new database (edit dbname below)

import psycopg2

file = open("logins.txt")
logins = [line.strip() for line in file.readlines()]

def main():
	conn = psycopg2.connect(host="database.rhodescs.org", user="kirlinp", password="kirlinp", dbname="practice")
	cur = conn.cursor()

	for username in logins:
		username_quoted = '"' + username + '"'
		print("Doing " + username)
	
		cur.execute("DROP SCHEMA IF EXISTS \"" + username + "\" CASCADE;")
		cur.execute("CREATE SCHEMA AUTHORIZATION \"" + username + "\";")
		cur.execute("GRANT ALL PRIVILEGES ON SCHEMA \"" + username + "\" TO \"" + username + "\";");
		
	conn.commit()
	cur.close()
	conn.close()
	

main()
