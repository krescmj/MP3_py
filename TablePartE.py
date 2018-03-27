import happybase as hb

import happybase as hb

conn = hb.Connection()

table = conn.table('powers')

#columns = (b'personal:name', b'personal:city')

for key, data in table.scan(include_timestamp=True):
    print('Found: {}, {}'.format(key, data))

conn.close()

