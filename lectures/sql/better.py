import psycopg2

logins = ["sample"]
file = open("logins.txt")
logins = [line.strip() for line in file.readlines()]

def main():
	conn = psycopg2.connect(host="dbclass.rhodescs.org", user="kirlinp", password="kirlinp", dbname="potter")
	cur = conn.cursor()

	for username in logins:
		username_quoted = '"' + username + '"'
		print("Doing " + username)
	
		cur.execute("DROP SCHEMA IF EXISTS \"" + username + "\" CASCADE;")
		cur.execute("CREATE SCHEMA AUTHORIZATION \"" + username + "\";")
		cur.execute("GRANT ALL PRIVILEGES ON SCHEMA \"" + username + "\" TO \"" + username + "\";");
		do_potter(cur, username)
		
	conn.commit()
	cur.close()
	conn.close()
	
	conn = psycopg2.connect(host="dbclass.rhodescs.org", user="kirlinp", password="kirlinp", dbname="flights")
	cur = conn.cursor()

	for username in logins:
		username_quoted = '"' + username + '"'
		print("Doing " + username)
	
		cur.execute("DROP SCHEMA IF EXISTS \"" + username + "\" CASCADE;")
		cur.execute("CREATE SCHEMA AUTHORIZATION \"" + username + "\";")
		cur.execute("GRANT ALL PRIVILEGES ON SCHEMA \"" + username + "\" TO \"" + username + "\";");
		do_flights(cur, username)
		
	conn.commit()
	cur.close()
	conn.close()

		
def do_flights(cur, username):
	print("Doing flights for", username)
	username_quoted = '"' + username + '"'
	
	cur.execute(f"""
	
	
DROP TABLE IF EXISTS {username_quoted}.airlines;
DROP TABLE IF EXISTS {username_quoted}.airports;
DROP TABLE IF EXISTS {username_quoted}.customers;
DROP TABLE IF EXISTS {username_quoted}.schedule;
DROP TABLE IF EXISTS {username_quoted}.bookings;

CREATE TABLE {username_quoted}.airlines (
	name		varchar NOT NULL,
	airlineCode	char(2) NOT NULL,
	PRIMARY KEY(airlineCode)
);

CREATE TABLE {username_quoted}.airports (
	name	VARCHAR,
	airportCode	char(3),
	city	VARCHAR,
	state	VARCHAR,
	airportLat	REAL,
	airportLong	REAL,
	cityLat	REAL,
	cityLong	REAL,
	population	INT,
	PRIMARY KEY(airportCode)
);

CREATE TABLE {username_quoted}.customers (
	customerID	INTEGER NOT NULL,
	first	VARCHAR NOT NULL,
	last	VARCHAR NOT NULL,
	city	VARCHAR NOT NULL,
	state	VARCHAR NOT NULL,
	birthday	DATE,
	PRIMARY KEY(customerID)
);

CREATE TABLE {username_quoted}.schedule (
	airlineCode VARCHAR, 
	flightNumber int, 
	source VARCHAR, 
	destination VARCHAR, 
	departTime TIME, 
	arriveTime TIME, 
	constraint pk_schedule primary key(airlineCode, flightNumber) );
	
CREATE TABLE {username_quoted}.bookings(customerID int, airlineCode varchar, flightNumber int, boardingGroup int, seatRow int, seatLetter char(1),
	 constraint pk_bookings primary key(customerID, airlineCode, flightNumber)
	 
);

	""")
	
	cur.execute(f"GRANT ALL PRIVILEGES ON {username_quoted}.airlines TO \"" + username + "\";");
	cur.execute(f"GRANT ALL PRIVILEGES ON {username_quoted}.airports TO \"" + username + "\";");
	cur.execute(f"GRANT ALL PRIVILEGES ON {username_quoted}.customers TO \"" + username + "\";");
	cur.execute(f"GRANT ALL PRIVILEGES ON {username_quoted}.schedule TO \"" + username + "\";");
	cur.execute(f"GRANT ALL PRIVILEGES ON {username_quoted}.bookings TO \"" + username + "\";");
	
	file = open("flights-airlines.csv", "r")
	cur.copy_expert(f"COPY {username_quoted}.airlines FROM STDIN (FORMAT CSV, DELIMITER ',')", file)
	file.close()
	
	file = open("flights-airports.csv", "r")
	cur.copy_expert(f"COPY {username_quoted}.airports FROM STDIN (FORMAT CSV, DELIMITER ',')", file)
	file.close()
	
	file = open("flights-customers.csv", "r")
	cur.copy_expert(f"COPY {username_quoted}.customers FROM STDIN (FORMAT CSV, DELIMITER ',')", file)
	file.close()
	
	file = open("flights-schedule.csv", "r")
	cur.copy_expert(f"COPY {username_quoted}.schedule FROM STDIN (FORMAT CSV, DELIMITER ',')", file)
	file.close()
	
	file = open("flights-bookings.csv", "r")
	cur.copy_expert(f"COPY {username_quoted}.bookings FROM STDIN (FORMAT CSV, DELIMITER ',')", file)
	file.close()

	
def do_potter(cur, username):
	print("Doing potter for", username)
	username_quoted = '"' + username + '"'
	cur.execute(f"""
	
DROP TABLE IF EXISTS {username_quoted}.students;
DROP TABLE IF EXISTS {username_quoted}.profs;
DROP TABLE IF EXISTS {username_quoted}.courses;
DROP TABLE IF EXISTS {username_quoted}.heads;
DROP TABLE IF EXISTS {username_quoted}.rooms;
DROP TABLE IF EXISTS {username_quoted}.grades;

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
	
	cur.execute(f"GRANT ALL PRIVILEGES ON {username_quoted}.students TO \"" + username + "\";");
	cur.execute(f"GRANT ALL PRIVILEGES ON {username_quoted}.profs TO \"" + username + "\";");
	cur.execute(f"GRANT ALL PRIVILEGES ON {username_quoted}.grades TO \"" + username + "\";");
	cur.execute(f"GRANT ALL PRIVILEGES ON {username_quoted}.rooms TO \"" + username + "\";");
	cur.execute(f"GRANT ALL PRIVILEGES ON {username_quoted}.courses TO \"" + username + "\";");
	cur.execute(f"GRANT ALL PRIVILEGES ON {username_quoted}.heads TO \"" + username + "\";");
	
	file = open("potter-students.csv", "r")
	cur.copy_expert(f"COPY {username_quoted}.students FROM STDIN (FORMAT CSV, DELIMITER ',')", file)
	file.close()
	
	file = open("potter-profs.csv", "r")
	cur.copy_expert(f"COPY {username_quoted}.profs FROM STDIN (FORMAT CSV, DELIMITER ',')", file)
	file.close()
	
	file = open("potter-grades.csv", "r")
	cur.copy_expert(f"COPY {username_quoted}.grades FROM STDIN (FORMAT CSV, DELIMITER ',')", file)
	file.close()
	
	file = open("potter-rooms.csv", "r")
	cur.copy_expert(f"COPY {username_quoted}.rooms FROM STDIN (FORMAT CSV, DELIMITER ',')", file)
	file.close()
	
	file = open("potter-courses.csv", "r")
	cur.copy_expert(f"COPY {username_quoted}.courses FROM STDIN (FORMAT CSV, DELIMITER ',')", file)
	file.close()
	
	file = open("potter-heads.csv", "r")
	cur.copy_expert(f"COPY {username_quoted}.heads FROM STDIN (FORMAT CSV, DELIMITER ',')", file)
	file.close()
	

main()
