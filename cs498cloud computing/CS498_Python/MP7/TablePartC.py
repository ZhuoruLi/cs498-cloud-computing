import happybase as hb
import csv

connection = hb.Connection()
table = connection.table('powers')

with open('input.csv') as file_obj:  
    # Create reader object by passing the file 
    # object to reader method
    # heading = next(file_obj)
    reader_obj = csv.reader(file_obj, delimiter=',', quotechar='|')
    print(reader_obj)
    # Iterate over each row in the csv 
    # file using reader object
    for row in reader_obj:
        #row-key = row[0]
        #table.put(row[0]: )
        val = {b'personal:hero': row[1], b'personal:power': row[2], b'professional:name': row[3], b'professional:xp': row[4], b'custom:color': row[5]}
        table.put(row[0], val)

connection.close()

# table.put(b'row-key', {b'cf:col1': b'value1',
#                        b'cf:col2': b'value2'})

# data = {
#     b'personal:name': b'Raju',
#     b'personal:city': b'Hyderabad',
#     b'professional:designation': b'Manager',
#     b'professional:salary': b'50000'
# }

# table.put(b'row1', data)

