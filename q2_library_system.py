def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)


def borrow_book(catalog, borrowed_books, book_id):
    if book_id not in catalog:
        print(f"❌ Error: Book ID {book_id} does not exist.")
        return
    if book_id in borrowed_books:
        print(f"❌ Error: Book ID {book_id} is already borrowed.")
        return
    borrowed_books.append(book_id)
    print(f"📖 Successfully borrowed: '{catalog[book_id][0]}'")


def show_borrowed(catalog, borrowed_books):
    print("\n📋 --- Borrowed Books ---")
    if not borrowed_books:
        print("No books are currently borrowed.")
    else:
        for book_id in borrowed_books:
            title, author, year = catalog[book_id]
            print(f"ID: {book_id} | '{title}' by {author} ({year})")
    print("-------------------------\n")

def main():
    catalog = {}
    borrowed_books = []

    while True:
        print("=== Library Menu ===")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. View Borrowed Books")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            while True:
                try:
                    book_id = int(input("Enter Book ID: "))
                    if book_id in catalog:
                        print("❌ Error: Book ID already exists.")
                        continue
                    break
                except ValueError:
                    print("❌ Invalid: ID must be an integer.")
            
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            
            while True:
                try:
                    year = int(input("Enter Year: "))
                    break
                except ValueError:
                    print("❌ Invalid: Year must be an integer.")
                    
            add_book(catalog, book_id, title, author, year)
            print("✅ Book added successfully.")

        elif choice == "2":
            while True:
                try:
                    book_id = int(input("Enter Book ID to borrow: "))
                    break
                except ValueError:
                    print("❌ Invalid: ID must be an integer.")
            borrow_book(catalog, borrowed_books, book_id)

        elif choice == "3":
            show_borrowed(catalog, borrowed_books)

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
