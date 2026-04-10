from mysql import connector

class MobileListCreateRetrieveUpdateDelete:

    def __init__(self):
        self.connection = connector.connect(
            host = "localhost",
            user = "root",
            password = "Adithya2003@",
            database = "mobile_db"
        )

        self.cursor = self.connection.cursor()
        print("db connection ok...")

    def list(self):
        query = "select * from mobile"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        if records:
            for row in records:
                print(row)
        else:
            print("no records found")

    def create(self,title=None,brand=None,specs=None,price=None):
        query = """
                insert into mobile(title,brand,specs,price) values(%s,%s,%s,%s)
            """
        data = (title,brand,specs,price)
        self.cursor.execute(query,data)
        self.connection.commit()
        print("data inserted successfully")

    def retrieve(self,id=None):
        query = "select * from mobile where id = %s"
        data = (id,)
        self.cursor.execute(query,data)
        record = self.cursor.fetchone()
        if record:
            print(record)
        else:
            print("no record found...")

    def delete(self,id=None):
        query = "delete from mobile where id = %s"
        data = (id,)
        self.cursor.execute(query,data)
        self.connection.commit()
        print("record deleted...")
    
mobile_instance = MobileListCreateRetrieveUpdateDelete()
#mobile_instance.create("iPhone 15 Pro Max","Apple","8 GB",159000)
#mobile_instance.list()
mobile_instance.retrieve(1)