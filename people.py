
import psycopg2
connection =  psycopg2.connect("dbname=library user=Philips password=philipsjohn@2001 host=localhost port=5432")
#def main():
   # connection =  psycopg2.connect("dbname=library user=Philips password=philipsjohn@2001 host=localhost port=5432")
    #connection.commit()
    #connection.close()

def insert_sample_books(connection): 
     sample_books = [(1,'to kill a mockingbird', 'steve greens', '250403065', 'romance', 1984, 30),
                (2, 'half of a yellow sun', 'chinua achebe', '250403066', 'thriller', 2002, 17),
                (3, 'wuthering heights', 'lionel dave', '250403067', 'romance', 2012, 22),
                (4, 'voicenotes for isabelle', 'nens coffee', '250403068', 'romcom', 2024, 12),
                (5, 'far from home', 'victor eden', '250403069', 'horror', 1867, 37) 
        ]
     with connection:
        with connection.cursor() as cursor:
            cursor.executemany("""INSERT INTO mini_library(id, title, author, isbn, genre, publication_year, available_copies) VALUES(%s, %s, %s, %s, %s, %s, %s) ON CONFLICT(isbn) DO NOTHING""", sample_books )
    
        
def get_book_by_id(connection, book_id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM mini_library WHERE id = %s", (book_id,))
            return cursor.fetchall()
   
def update_available_copies(copies, book_id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("""UPDATE mini_library SET available_copies = %s WHERE id = %s """, (copies, book_id))

def remove_sample_books(sample_books):
    with connection :
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM mini_library WHERE id = %s", (sample_books,))

    # cursor.close()
    # connection.close()



roles_info = [(1, 'blossom_onyeka', 'password.2023', 'user'),
              (2, 'henry_lewis', 'derter.2024', 'user')
            ]

def insert_roles_info(connection):
    roles_info = [(1, 'blossom_onyeka', 'password.2023', 'user'),
              (2, 'henry_lewis', 'derter.2024', 'user')
            ]
    with connection:
        with connection.cursor() as cursor:
            cursor.executemany("""INSERT INTO roles(id, username, password, role) VALUES(%s, %s, %s, %s) ON CONFLICT(id) DO NOTHING;""", roles_info )
        



def insert_sample_loans(sample_loans):
    sample_loans = [(1, 'alice jones'),
                (2, 'henry chicken'),
                (3, 'jones adams')] 
    with connection:
        with connection.cursor() as cursor:
            cursor.executemany("""INSERT INTO loans(book_id, borrower_name) VALUES(%s, %s)""", sample_loans  )

       
def get_loans_by_id(loan_id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("""SELECT 
                loans.loan_id,
                loans.borrower_name,
                mini_library.title,
                mini_library.author,
                loans.borrow_date
                FROM loans 
                JOIN mini_library ON loans.book_id = mini_library.id
                WHERE loans.loan_id = %s
                """, (loan_id,))   
            return cursor.fetchall()
            
def remove_sample_loans(sample_loans):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("""DELETE FROM loans WHERE book_id = %s AND borrower_name =%s""", (sample_loans,))
        


purchased_books = [(6, 'sherlingstock', 'lucia banks', '250403070', 'documentary', 2026, 57)
                   ]

#references foreign key
#joining two different tables

#print("borrowed books(INNER JOIN)")
#for record in cursor.fetchall() :
   # print(record)

#cursor.execute("SELECT * FROM diction")
#print(cursor.fetchall())  

#insert_sample_books(stress)
#new_book = get_book_by_id(7)
#print(new_book)

#update_available_copies(20, 7)
#new_book = get_book_by_id(7)
#print(new_book)

#remove_sample_books(7)

#remaining = get_all_books()
#for book in remaining :
    #print(book)    

if __name__ == '__main__':
   get_book_by_id(connection, 1)