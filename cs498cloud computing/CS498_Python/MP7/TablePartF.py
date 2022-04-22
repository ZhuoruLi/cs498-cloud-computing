import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER

connection = hb.Connection()
table = connection.table('powers')

for key, row in table.scan():
    color = row[b'custom:color']
    name = row[b'professional:name']
    power = row[b'personal:power']
    for key, row1 in table.scan():
        color1 = row1[b'custom:color']
        name1 = row1[b'professional:name']
        power1 = row1[b'personal:power']
        if color == color1 and name != name1:
            print('{}, {}, {}, {}, {}'.format(name, power, name1, power1, color))
        

# for i in range(1, 26):
#     #row = table.row('row%d' % i)
#     color = row[b'custom:color']
#     name = row[b'professional:name']
#     power = row[b'personal:power']
#     for j in range(1, 26):
#         row1 = table.row('row%d' % j)
#         color1 = row1[b'custom:color']
#         name1 = row1[b'professional:name']
#         power1 = row1[b'personal:power']
#         if color == color1 and name != name1:
#             print('{}, {}, {}, {}, {}'.format(name, power, name1, power1, color))

connection.close()