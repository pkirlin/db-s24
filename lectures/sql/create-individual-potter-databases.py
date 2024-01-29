# run this as superuser, connected to the potter db

import sys

file = open("logins.txt", "r")
cwd = "/Users/pkirlin/box/work/courses/db-s22/web/lectures/sql"

for line in file:
	username = line.strip()
	username_quoted = '"' + username + '"'

	# create their schema
	print("DROP SCHEMA IF EXISTS \"" + username + "\" CASCADE;")
	print("CREATE SCHEMA AUTHORIZATION \"" + username + "\";")

	# create tables
	print(f"""
CREATE TABLE IF NOT EXISTS {username_quoted}.students
(
    slast character varying,
    sfirst character varying,
    house character varying,
    pet character varying
);

CREATE TABLE IF NOT EXISTS {username_quoted}.rooms
(
    room character varying,
    maxseats integer
);

CREATE TABLE IF NOT EXISTS {username_quoted}.profs
(
    plast character varying,
    pfirst character varying
);

CREATE TABLE IF NOT EXISTS {username_quoted}.heads
(
    house character varying,
    plast character varying
);

CREATE TABLE IF NOT EXISTS {username_quoted}.courses
(
    crn integer,
    year integer,
    name character varying,
    plast character varying,
    starttime integer,
    room character varying
);

CREATE TABLE IF NOT EXISTS {username_quoted}.grades
(
    slast character varying,
    crn integer,
    grade integer
);
	""")

	print("GRANT ALL PRIVILEGES ON SCHEMA \"" + username + "\" TO \"" + username + "\";");
	print(f"GRANT ALL PRIVILEGES ON {username_quoted}.students TO \"" + username + "\";");
	print(f"GRANT ALL PRIVILEGES ON {username_quoted}.profs TO \"" + username + "\";");
	print(f"GRANT ALL PRIVILEGES ON {username_quoted}.grades TO \"" + username + "\";");
	print(f"GRANT ALL PRIVILEGES ON {username_quoted}.rooms TO \"" + username + "\";");
	print(f"GRANT ALL PRIVILEGES ON {username_quoted}.courses TO \"" + username + "\";");
	print(f"GRANT ALL PRIVILEGES ON {username_quoted}.heads TO \"" + username + "\";");


# switch to psql

file = open("logins.txt", "r")

for line in file:
	username = line.strip()
	username_quoted = '"' + username + '"'

	# put data in tables
	print(f"""	
\copy {username_quoted}.students from '{cwd}/potter-students.csv' delimiter ',' csv;

\copy {username_quoted}.profs from '{cwd}/potter-profs.csv' delimiter ',' csv;

\copy {username_quoted}.heads from '{cwd}/potter-heads.csv' delimiter ',' csv;

\copy {username_quoted}.courses from '{cwd}/potter-courses.csv' delimiter ',' csv;

\copy {username_quoted}.grades from '{cwd}/potter-grades.csv' delimiter ',' csv;

\copy {username_quoted}.rooms from '{cwd}/potter-rooms.csv' delimiter ',' csv;
	""")
