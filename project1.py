import psycopg2
connection =  psycopg2.connect("dbname=library user=Philips password=philipsjohn@2001 host=localhost port=5432")
cursor = connection.cursor()

class DatabaseConnectionError(Exception):
    pass
class AuditExceptionError(Exception):
    pass

class LibraryAudit() :
    def __init__(self, db_string):
        try: 
            self.connection = psycopg2.connect(db_string)
            self.cursor = self.connection.cursor()
        except psycopg2.Error as e:
            raise DatabaseConnectionError(f"failed to connect to database: {e}")

    def get_total_books(self):
        try:
            self.cursor.execute("SELECT COUNT(*) FROM mini_library")
        except psycopg2.Error as e:
            raise AuditExceptionError(f"failed to get total books: {e}")

    def get_low_stock_alerts(self, limit):
        if not isinstance(limit, int) or limit < 0:
            raise ValueError('limit must be a positive integer')
        try:
            self.cursor.execute("SELECT id, title, available_copies FROM mini_library WHERE available_copies < %s", (limit,))
            filtered_books = self.cursor.fetchall()
            for book_id, title, copies in filtered_books:
                print(f"Warning: '{title}' only has {copies} copies left!")
        except psycopg2.Error as e:
            raise AuditExceptionError(f"failed to get minimum count: {e}")

    def close(self):
        self.connection.close()        

if __name__ == '__main__':
    db_config = "dbname=library user=Philips password=philipsjohn@2001 host=localhost port=5432"
    audit = LibraryAudit(db_config)








