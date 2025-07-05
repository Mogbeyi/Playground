#Claude's code
class LibrarySystem:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.loans = {}
    
    def handle_message(self, message_type, data):
        handlers = {
            'add_book': self._handle_add_book,
            'add_member': self._handle_add_member,
            'borrow_book': self._handle_borrow_book,
            'return_book': self._handle_return_book,
            'search_books': self._handle_search_books,
            'get_member_loans': self._handle_member_loans
        }
        return handlers[message_type](data)
    
    def _handle_add_book(self, data):
        book_id = len(self.books) + 1
        self.books[book_id] = {
            'title': data['title'],
            'author': data['author'],
            'available': True
        }
        return {'status': 'success', 'book_id': book_id}
    
    def _handle_add_member(self, data):
        member_id = len(self.members) + 1
        self.members[member_id] = {
            'name': data['name'],
            'email': data['email']
        }
        return {'status': 'success', 'member_id': member_id}
    
    def _handle_borrow_book(self, data):
        book_id = data['book_id']
        member_id = data['member_id']
        
        if book_id not in self.books or not self.books[book_id]['available']:
            return {'status': 'error', 'message': 'Book unavailable'}
            
        loan_id = len(self.loans) + 1
        self.loans[loan_id] = {
            'book_id': book_id,
            'member_id': member_id,
            'returned': False
        }
        self.books[book_id]['available'] = False
        
        return {'status': 'success', 'loan_id': loan_id}
    
    def _handle_return_book(self, data):
        loan_id = data['loan_id']
        if loan_id not in self.loans:
            return {'status': 'error', 'message': 'Loan not found'}
            
        self.loans[loan_id]['returned'] = True
        self.books[self.loans[loan_id]['book_id']]['available'] = True
        return {'status': 'success'}
    
    def _handle_search_books(self, data):
        query = data['query'].lower()
        results = [
            {'id': bid, **book}
            for bid, book in self.books.items()
            if query in book['title'].lower() or query in book['author'].lower()
        ]
        return {'status': 'success', 'results': results}
    
    def _handle_member_loans(self, data):
        member_id = data['member_id']
        active_loans = [
            {'loan_id': lid, **loan}
            for lid, loan in self.loans.items()
            if loan['member_id'] == member_id and not loan['returned']
        ]
        return {'status': 'success', 'loans': active_loans}

# Example usage
library = LibrarySystem()

# Adding a book
print(library.handle_message('add_book', {
    'title': 'The Hobbit',
    'author': 'J.R.R. Tolkien'
}))

# Adding a member
print(library.handle_message('add_member', {
    'name': 'John Doe',
    'email': 'john@example.com'
}))

# Borrowing a book
print(library.handle_message('borrow_book', {
    'book_id': 1,
    'member_id': 1
}))

# Searching books
print(library.handle_message('search_books', {
    'query': 'hobbit'
}))




#Deep-seek's code
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True  # Tracks whether the book is available

    def send_message(self, message, *args):
        if message == "borrow":
            return self.borrow()
        elif message == "return":
            return self.return_book()
        elif message == "status":
            return self.status()
        else:
            raise ValueError(f"Unknown message for Book: {message}")

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return f"Book '{self.title}' by {self.author} has been borrowed."
        else:
            return f"Book '{self.title}' is not available."

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            return f"Book '{self.title}' has been returned."
        else:
            return f"Book '{self.title}' was not borrowed."

    def status(self):
        return f"Book '{self.title}' by {self.author} is {'available' if self.is_available else 'not available'}."


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def send_message(self, message, *args):
        if message == "borrow_book":
            book = args[0]
            return self.borrow_book(book)
        elif message == "return_book":
            book = args[0]
            return self.return_book(book)
        elif message == "list_books":
            return self.list_books()
        else:
            raise ValueError(f"Unknown message for Member: {message}")

    def borrow_book(self, book):
        response = book.send_message("borrow")
        if "borrowed" in response:
            self.borrowed_books.append(book)
        return response

    def return_book(self, book):
        response = book.send_message("return")
        if "returned" in response:
            self.borrowed_books.remove(book)
        return response

    def list_books(self):
        if not self.borrowed_books:
            return f"{self.name} has no borrowed books."
        return f"{self.name}'s borrowed books: {[book.title for book in self.borrowed_books]}"


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def send_message(self, message, *args):
        if message == "add_book":
            book = args[0]
            return self.add_book(book)
        elif message == "add_member":
            member = args[0]
            return self.add_member(member)
        elif message == "find_book":
            title = args[0]
            return self.find_book(title)
        elif message == "list_books":
            return self.list_books()
        elif message == "list_members":
            return self.list_members()
        else:
            raise ValueError(f"Unknown message for Library: {message}")

    def add_book(self, book):
        self.books.append(book)
        return f"Added book '{book.title}' to the library."

    def add_member(self, member):
        self.members.append(member)
        return f"Added member '{member.name}' to the library."

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return f"Book with title '{title}' not found."

    def list_books(self):
        if not self.books:
            return "No books in the library."
        return "Books in the library: " + ", ".join([book.title for book in self.books])

    def list_members(self):
        if not self.members:
            return "No members in the library."
        return "Members: " + ", ".join([member.name for member in self.members])


# Example Usage
if __name__ == "__main__":
    # Create a library
    library = Library()

    # Add books to the library
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("1984", "George Orwell")
    library.send_message("add_book", book1)
    library.send_message("add_book", book2)

    # Add members to the library
    member1 = Member("Alice")
    member2 = Member("Bob")
    library.send_message("add_member", member1)
    library.send_message("add_member", member2)

    # List books and members
    print(library.send_message("list_books"))
    print(library.send_message("list_members"))

    # Members borrow books
    print(member1.send_message("borrow_book", book1))
    print(member2.send_message("borrow_book", book2))

    # List borrowed books
    print(member1.send_message("list_books"))
    print(member2.send_message("list_books"))

    # Members return books
    print(member1.send_message("return_book", book1))
    print(member2.send_message("return_book", book2))

    # Check book status
    print(book1.send_message("status"))
    print(book2.send_message("status"))


#chat-gpt's code
class Library:
    def __init__(self):
        self.books = {}
        self.users = {}
        self.handlers = {
            "add_book": self._add_book,
            "register_user": self._register_user,
            "borrow_book": self._borrow_book,
            "return_book": self._return_book
        }

    def _add_book(self, title):
        if title not in self.books:
            self.books[title] = "available"
            print(f"📚 Book '{title}' added to library.")
        else:
            print(f"⚠️ Book '{title}' already exists.")

    def _register_user(self, user):
        if user not in self.users:
            self.users[user] = []
            print(f"👤 User '{user}' registered.")
        else:
            print(f"⚠️ User '{user}' is already registered.")

    def _borrow_book(self, user, title):
        if user not in self.users:
            print(f"🚫 User '{user}' is not registered.")
            return
        if title not in self.books:
            print(f"🚫 Book '{title}' does not exist.")
            return
        if self.books[title] == "available":
            self.books[title] = user
            self.users[user].append(title)
            print(f"📖 '{title}' borrowed by '{user}'.")
        else:
            print(f"⛔ Book '{title}' is already borrowed by '{self.books[title]}'.")

    def _return_book(self, user, title):
        if user in self.users and title in self.users[user]:
            self.books[title] = "available"
            self.users[user].remove(title)
            print(f"✅ '{title}' returned by '{user}'.")
        else:
            print(f"🚫 '{title}' was not borrowed by '{user}'.")

    def send(self, message, *args):
        if message in self.handlers:
            self.handlers[message](*args)
        else:
            print(f"🚨 Unknown message: {message}")

# Usage
library = Library()

library.send("add_book", "1984")
library.send("add_book", "To Kill a Mockingbird")

library.send("register_user", "Alice")
library.send("register_user", "Bob")

library.send("borrow_book", "Alice", "1984")
library.send("borrow_book", "Bob", "1984")  # Book already borrowed

library.send("return_book", "Alice", "1984")
library.send("borrow_book", "Bob", "1984")  # Now Bob can borrow

