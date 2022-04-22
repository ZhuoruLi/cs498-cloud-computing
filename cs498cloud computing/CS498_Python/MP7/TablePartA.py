import happybase as hb

#connection = hb.Connection('somehost')
connection = hb.Connection()
connection.open()

connection.create_table(
    'powers',
    {'personal': dict(),
     'professional': dict(),
     'custom': dict(),  # use defaults
    }
)

connection.create_table(
    'food',
    {'nutrition': dict(),
     'taste': dict(), # use defaults
    }
)

#table = connection.table('powers')

connection.close()
#print(connection.tables())