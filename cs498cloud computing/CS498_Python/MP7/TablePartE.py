import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER

connection = hb.Connection()
table = connection.table('powers')

columns = (b'custom:color', b'personal:hero', b'personal:power', b'professional:name', b'professional:xp')

# for key, data in table.scan(columns=columns, include_timestamp=True):
#     print('Found: {}, {}'.format(key, data))

for key, data in table.scan(columns=columns, include_timestamp=True):
    print('Found: {}, {}'.format(key, data))


connection.close()