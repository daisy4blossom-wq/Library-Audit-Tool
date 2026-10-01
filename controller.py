import psycopg2
from exceptions import BookUnavailableError, UnauthorizedAccessError, MemberLimitExceededError  
connection = psycopg2.connect("dbname=library user=Philips password=philipsjohn@2001 host=localhost port=5432")

class LibraryController():
    def __init__(self, db_connection):
        self.connection = db_connection

    def value_error(self,book_id, loan_id):
        if book_id > 0 or loan_id > 0:
            raise ValueError("IDs must be positive integers")

    PERMISSIONS = {"borrow_book": ["Manager", "admin"], 
                    "register_member": ["admin"],
                    "search_catalog": ["user", "Manager", "admin"],
                    "return_book":["Manager", "admin"],
                    "loan_count": ["Manager", "admin"]
                    }

    def permission(self, action: str):
        self.cursor.execute("SELECT current_user;")
        current_role = self.cursor.fetchone()[0]
        allowedroles = self.PERMISSIONS.get(action, [])
        if current_role not in allowedroles:
            raise UnauthorizedAccessError("AUTHORIZED ACCESS DENIED!")
        

    def borrow_book(self, user_role: str, book_id: int, loan_id: int):
        self.permission(user_role, "borrow_book")
        cursor = self.connection.cursor()
        cursor.execute("SELECT available_copies FROM books where id = ?", (book_id,) )
        result = cursor.fetchone()
        if not result:
            raise BookUnavailableError("Book not found!") 
       
        if result[0] <= 0: 
            raise BookUnavailableError("Book is not available right now!")

        cursor.execute("UPDATE books SET available_copies = available_copies - 1 WHERE id = ?,  (book_id,) ")
        self.connection.commit()
        return (f"Book {book_id} successfully stored under Loan ID {loan_id}")


    def register_member(self,user_role, username, password, role):
        self.permission(user_role, "register_member")
        cursor = self.connection.cursor()
        cursor.execute("""INSERT OR IGNORE INTO roles (username, password, role) VALUES(?,?,?,?)""", (username, password,role ) )
        return
         
         

    def search_catalog(self, search):
        cursor = self.connection.cursor()
        query = f"%{search}"
        cursor.execute("SELECT id, title, author, isbn, genre, publication_year, available_copies FROM mini_library WHERE title LIKE ?", (query,))
        results = cursor.fetchall()
        if not results:
            print("No books found!") 
        return

    def return_book(self, user_role, book_id, loan_id):
        self.permission(user_role, "return_book")
        cursor = self.connection.cursor()
        cursor.execute("UPDATE books SET available_copies = available_copies + 1 WHERE id = ?,  (book_id,) ")
        self.connection.commit()

    def loan_count(self, user_role, loan_id):
        self.permission(user_role, "loan_count")
        cursor = self.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM loans WHERE loan_id = ? AND return_date IS NULL", (loan_id,) )
        activeloans = cursor.fetchone()[0]
        if activeloans >= 3:
            raise MemberLimitExceededError("Borrower has reached their borrow limit")

        cursor.execute("SELECT COUNT(*) FROM loans WHERE loan_id = ? AND return_date IS NULL AND borrower_date < DATE('now')", (loan_id,) )
        pastcount = cursor.fetchone()[0]
        if pastcount > 0:
            raise UnauthorizedAccessError("Borrower has overdue debts. Clear debts first!") 
        self.connection.close()       

if __name__ == '__main__':
    LibraryController("dbname=library user=Philips password=philipsjohn@2001 host=localhost port=5432")