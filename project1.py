import sqlite3
connection = sqlite3.connect('books.db')
cursor = connection.cursor()

class DatabaseConnectionError(Exception):
    pass
class AuditExceptionError(Exception):
    pass

class LibraryAudit() :
    def __init__(self, books_db):
        try: 
            self.connection = sqlite3.connect(books_db)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            raise DatabaseConnectionError(f"failed to connect to database: {e}")

    def get_total_books(self):
        try:
            self.cursor.execute("SELECT COUNT(*) FROM mini_library")
        except sqlite3.Error as e:
            raise AuditExceptionError(f"failed to get total books: {e}")

    def get_low_stock_alerts(self, limit):
        if not isinstance(limit, int) or limit < 0:
            raise ValueError('limit must be a positive integer')
        try:
            self.cursor.execute("SELECT id, title, available_copies FROM mini_library WHERE available_copies < ?", (limit,))
            filtered_books = self.cursor.fetchall()
            for book_id, title, copies in filtered_books:
                print(f"Warning: '{title}' only has {copies} copies left!")
        except sqlite3.Error as e:
            raise AuditExceptionError(f"failed to get minimum count: {e}")

    def close(self):
        self.connection.close()        

audit = LibraryAudit('books.db')

audit.get_total_books()
audit.get_low_stock_alerts(20)
audit.close()    








