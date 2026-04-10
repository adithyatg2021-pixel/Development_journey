from mysql import connector

connection = connector.connect(
    host = "localhost",
    user = "root",
    password = "Adithya2003@",
    database = "gosell_db"
)

cursor = connection.cursor()
query = """
create table vehicle(
    id int auto_increment primary key,
    name varchar(200) not null unique,
    model varchar(200) not null,
    running_km varchar(100) not null,
    fuel_type enum("petrol","diesel","hybrid","electric","hidrogen fuel","biofuel"),
    owner_type varchar(200) not null,
    place varchar(200) not null,
    owner varchar(200) not null
)
"""

cursor.execute(query)
connection.commit()

cursor.close()
connection.close()
