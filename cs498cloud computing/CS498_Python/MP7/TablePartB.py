import happybase as hb
connection = hb.Connection()
print(connection.tables())
