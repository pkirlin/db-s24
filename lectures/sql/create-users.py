# run this as superuser, database connection doesn't matter

import sys

file = open("logins.txt", "r")

for line in file:
	username = line.strip()
	username_quoted = '"' + username + '"'

	# create the user
	print("DROP USER IF EXISTS \"" + username + "\";")
	print("CREATE USER \"" + username + "\" WITH PASSWORD '" + username + "';")

	# create their schema
	print("DROP SCHEMA IF EXISTS \"" + username + "\";")
	print("CREATE SCHEMA \"" + username + "\";")
	print("GRANT ALL ON SCHEMA \"" + username + "\" TO \"" + username + "\";");

