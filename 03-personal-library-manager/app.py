import json

def load_books(Filename:str):
    try:
        with open (Filename, 'r')as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []
    
        
def save_books(books, Filename:str):
    with open(Filename, 'w') as file:
        json.dump(books, file, indent=4)
    
def display_menu():
    print('1. Add book')
    print('2. Remove book')
    print('3. Search book')
    print('4. Display books')
    print('5. Display statistics')
    print('6. Exit')
    
def add_book(books):
    title = input('Enter title: ')
    author = input('Enter author: ')
    try:
        publication_year = int(input('Enter publication year: '))
    except ValueError:
        print("Invalid input for publication year. Please enter a valid year.")
        return  # Exit function if input is invalid
    generation = input('Enter generation: ')
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    
    books.append({
        "title": title,
        "author": author,
        "year": publication_year,
        "generation": generation,
        "read": read_status
    })

    save_books(books, 'library.txt')  # Save updated list

    print('\nBook added successfully!\n')

def remove_book(books):
    title = input('Enter the title of the book to remove: ')
    for book in books:
        if book['title'].lower() == title.lower():  # Case-insensitive match
            books.remove(book)
            save_books(books, 'library.txt')  # Save updated list
            print('\nBook removed successfully!\n')
            return  # Exit after removing the book to prevent further iterations

    # This runs only if no book was found
    print('\nBook not found.\n')
    
    
def search_book(books):
    print('Search By')
    print('1. Title')
    print('2. Author')
    
    user_input = input('Enter your choice: ')
    if user_input == '1':
        title = input('Enter title: ')
        for book in books:
            if book['title'].lower() == title.lower():  # Case-insensitive match
                
                print('\n_______________________\n')
                print(f"Title: {book['title']}")
                print(f"Author: {book['author']}")
                print(f"Publication Year: {book['year']}")
                print(f"Generation: {book['generation']}")
                print(f"Read Status: {'Yes' if book['read'] else 'No'}")
                print('\n_______________________\n')
                if book['read']:
                    return  # Exit after printing the book to prevent further iterations
            print('\nBook not found.\n')
    elif user_input == '2':
        author = input('Enter author: ')
        for book in books:
            if book['author'].lower() == author.lower():  # Case-insensitive match
                print('\n_______________________\n')
                print(f"Title: {book['title']}")
                print(f"Author: {book['author']}")
                print(f"Publication Year: {book['year']}")
                print(f"Generation: {book['generation']}")
                print(f"Read Status: {'Yes' if book['read'] else 'No'}")
                print('\n_______________________\n')
                if book['read']:
                    return  # Exit after printing the book to prevent further iterations
            print('\nBook not found.\n')
def display_books(books):
    if not books:
        print('\nLibrary is empty.\n')
        return
    
    print('\n All books of Library\n')
    print('\n_______________________\n')
    for i,book in enumerate(books,1):
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['generation']} - {'Read' if book['read'] else 'Unread'}")
    print('\n_______________________\n')
    
def display_statistics(books):
    total_books = len(books)
    read_books = sum(1 for book in books if book['read'])
    unread_books = sum(1 for book in books if not book['read'])
    
    print("\nStatistics:\n")
    print(f"Total books: {total_books}")
    if total_books > 0:
        print(f"Percentage read: {read_books / total_books * 100:.2f}%\n")
    else:
        print("Percentage read: 0.00%\n")
        
    
def main():
    books = load_books('library.txt')
    while True:
        display_menu()
        choice = input('Enter choice (1-6): ')
        if choice == '1':
            add_book(books)
        elif choice == '2':
            remove_book(books)
        elif choice == '3':
            search_book(books)
        elif choice == '4':
            display_books(books)
        elif choice == '5':
            display_statistics(books)
        elif choice == '6':
            break
        else:
            print('\nInvalid choice. Please try again.\n')



if __name__ == '__main__':
    main()