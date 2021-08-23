from faker import Faker
from random import randint
from datetime import date, timedelta
from mysql.connector import MySQLConnection

fake = Faker()


base_date = date(1970, 1, 1)
insert_string = '''
USE cbtnuggets_indexes;
START TRANSACTION;
INSERT INTO people (firstName, lastName, birthDate) VALUES'''

for x in range(100000):
  birthDate = base_date + timedelta(days=randint(1,18500))
  firstName = fake.first_name()
  lastName = fake.last_name()
  #print(firstName)
  new_string = f"\n  ('{firstName}', '{lastName}', '{birthDate}'),"
  insert_string = insert_string + new_string

insert_string = insert_string[0:len(insert_string)-1] + ';'
insert_string = insert_string + "\nCOMMIT;"

print(insert_string)
print('Finished generating people')
#exit()

try:
  connection = MySQLConnection(user='root', password='cbt123', host='127.0.0.1', port='34422')

  cursor = connection.cursor()
  result = cursor.execute(insert_string, multi=True)
  for item in result:
    print('Ran statement')
    print(item)
    pass

  connection.commit()
  print('Committed rows to table')
finally:
  connection.close()
