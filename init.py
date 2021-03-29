import sqlalchemy as db

#engine = db.create_engine('sqlite:///data.db')
engine = db.create_engine('sqlite:///test.sqlite3')
connection = engine.connect()
metadata = db.MetaData()
shows = db.Table('Nodos', metadata, autoload=True, autoload_with=engine)
query = db.select([shows])
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
print(result_set)