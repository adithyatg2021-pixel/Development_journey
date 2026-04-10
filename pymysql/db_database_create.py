from mysql import connector

connection = connector.connect(
    host = "localhost",
    user = "root",
    password = "Adithya2003@"
)

cursor = connection.cursor()
query = "create database py_db"
cursor.execute(query)
connection.commit()
print("completed")

