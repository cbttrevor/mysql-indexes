from mysql.connector import MySQLConnection

create_database = '''
DROP DATABASE IF EXISTS cbtnuggets_indexes;
CREATE DATABASE IF NOT EXISTS cbtnuggets_indexes;
USE cbtnuggets_indexes;

DROP TABLE IF EXISTS people;
CREATE TABLE IF NOT EXISTS people
  (
    person_id INT AUTO_INCREMENT PRIMARY KEY,
    firstName varchar(30) NOT NULL,
    lastName varchar(30) NOT NULL,
    birthDate DATE NOT NULL
  );

'''

connection = MySQLConnection(user='root', password='cbt123', port='34422', host='127.0.0.1')
cursor = connection.cursor()

result = cursor.execute(create_database, multi=True)

for statement in result:
    print(statement)
