from mysql import connector

connection = connector.connect(
    host = "localhost",
    user = "root",
    password = "Adithya2003@",
    database = "py_db"
)

cursor = connection.cursor()
query = """
delete from sports where id = %s
"""
data = (1,)

cursor.execute(query,data)
connection.commit()
cursor.close()
connection.close()
print("Record deleted....")