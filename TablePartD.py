import happybase as hb

conn = hb.Connection()

table = conn.table('powers')

row = table.row(b'row1')
 
print('hero: {}, power: {}, name: {}, xp: {}, color: {}'.format(row[b'personal:hero'], 
															    row[b'personal:power'], 
																row[b'professional:name'],
																row[b'professional:xp'],
																row[b'custom:color']))

row = table.row(b'row19')

print('hero: {}, color: {}'.format(row[b'personal:hero'], 
								   row[b'custom:color']))
								   
row = table.row(b'row1')
 
print('hero: {}, name: {}, color: {}'.format(row[b'personal:hero'], 
											 row[b'professional:name'],
											 row[b'custom:color']))
conn.close()

