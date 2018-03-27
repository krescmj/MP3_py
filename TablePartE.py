import happybase as hb

conn = hb.Connection()

table = conn.table('powers')

for key, data in table.scan(include_timestamp=True):
    print('Found: {}, {}'.format(key, data))

conn.close()

