from controller import LibraryController 
import psycopg2
from exceptions import BookUnavailableError, UnauthorizedAccessError, MemberLimitExceededError  
import people 

def cli():
    connection =  psycopg2.connect("dbname=library user=Philips password=philipsjohn@2001 host=localhost port=5432")
    controller = LibraryController(connection)
    print("\nHello!, welcome to the library.")
    current_user = None
    current_role = None
    while True:
        if not current_user:
            print("1. Login")
            print("2. Search")
            print("3. Exit")
            choice = input("Select an option:")  

        if choice == "1":
            username = input("Username:")
            password = input("password:")

            cursor = connection.cursor()
            cursor.execute("SELECT role FROM roles WHERE username = %s AND password =%s", (username, password) )
            result = cursor.fetchone()

            if result:
                current_user = username
                current_role = result[0]
                print(f"\n SUCCESS: logged in as {current_user} {current_role}")    
            else:
                print(f"\n ERROR: Invalid username or password")  


        elif choice == "2":
            search_item = input ("Enter book title to search:")
            results = controller.search_catalog(search_item)
            if not results:
                print("book not found")
            else:
                print("Search results...") 
                for book in results:
                    print(f"ID: {book[0]} | Title: {book[1]} | Author: {book[2]} | Genre: {book[3]}")   

        elif choice == "3":
            print("Goodbye.")
            break    

