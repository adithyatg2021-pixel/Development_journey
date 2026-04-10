from mysql import connector

class BookListRetrieveCreateUpdateDelete:

    def __init__(self):
        try:
            self.connection = connector.connect(
            host = "localhost",
            user = "root",
            password = "Adithya2003@",
            database = "book_db"
            )

            self.cursor = self.connection.cursor()

            print("db connection ok....")
        
        except Exception as e:
            print(e)

    def list(self):
        query = "select * from book"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        if records:
            for row in records:
                print(row)
        else:
            print("no records found...")

    def create(self,title=None,author=None,price=None,publisher=None,genre=None,year=None):
        query = """
                insert into book(title,author,price,publisher,genre,year) values(%s,%s,%s,%s,%s,%s)
            """
        data = (title,author,price,publisher,genre,year)
        self.cursor.execute(query,data)
        self.connection.commit()
        print("Record inserted...")

    def retrieve(self,id=None):
        query = "select * from book where id = %s"
        data=(id,)
        self.cursor.execute(query,data)
        record = self.cursor.fetchone()
        if record:
            print(record)
        else:
            print("no record found...")

    def delete(self,id=None):
        query = "delete from book where id = %s"
        data = (id,)
        self.cursor.execute(query,data)
        self.connection.commit()
        print("record deleted...")

    def update(self,id=None,**kwargs):

        place_holder = ""
        for k in kwargs.keys():
            place_holder += f"{k}=%s,"
        place_holder = place_holder.rstrip(",")
        query = f"update book set {place_holder} where id={id}"
        data = [v for v in kwargs.values()]
        self.cursor.execute(query,data)
        self.connection.commit()
        print("data updated")

book_instance = BookListRetrieveCreateUpdateDelete()
#book_instance.create("Randamoozham","mt",500,"abc","fiction",1997)
book_instance.list()
# book_instance.retrieve(2)
# book_instance.delete(1)
#book_instance.update(id=2,price=800)