import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Nodos
              (Firm TEXT, Model TEXT, Price INT, Birth DATETIME, Death DATETIME, Unity TEXT, Data INT, Quality INT, Category TEXT)''')

cursor.execute('''INSERT INTO Nodos (Firm, Model, Price, Birth, Death, Unity, Data, Quality, Category) 
              VALUES ('Test', 'Testm', 5, '2007-01-01 10:00:00', NULL, 'g', 2, 6, 'Aseo')''')


connection.commit()
connection.close()