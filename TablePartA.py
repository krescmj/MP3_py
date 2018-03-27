import happybase as hb

conn = hb.Connection()

p_cf = {
    'personal': dict(),
    'professional': dict(),
	'custom': dict()
}

f_cf = {
    'nutrition': dict(),
    'taste': dict()
}

conn.create_table('powers', p_cf)
conn.create_table('food', f_cf)

conn.close()
