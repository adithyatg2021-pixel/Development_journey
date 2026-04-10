from mysql import connector

connection = connector.connect(
    host = "localhost",
    user = "root",
    password = "Adithya2003@",
    database = "py_db"
)

cursor = connection.cursor()
query = """
select * from sports where id = %s
"""
data = (2,)
cursor.execute(query,data)
records = cursor.fetchone()
print(records)
cursor.close()
connection.close()