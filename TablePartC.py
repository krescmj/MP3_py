import happybase as hb
import csv

conn = hb.Connection()

table = conn.table('powers')

with open('input.csv') as csvfile:
	data = csv.reader(csvfile, delimiter=',')
	for row in data:
		data = {
			b'personal:hero':     row[1],
			b'personal:power':    row[2],
			b'professional:name': row[3],
			b'professional:xp':   row[4],
			b'custom:color':      row[5]
		}

		table.put(row[0], data)

conn.close()
