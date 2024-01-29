import sys

for line in sys.stdin:
	line = line.strip()
	pieces = line.split('\t')
	email = pieces[1]
	pieces = email.split('@')
	print(pieces[0])
