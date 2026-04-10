from mysql import connector

connection = connector.connect(
    host = "localhost",
    user = "root1",
    password = "Adithya2003@"
)

print(connection)