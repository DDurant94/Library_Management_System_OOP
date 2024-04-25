import re
class Book:
  def __init__ (self,title, author, isbn, genre, publication_date):
    self.__title = title
    self.__author = author
    self.__isbn = isbn
    self.__genre = genre
    self.__publication_date = publication_date
    self.availability_status = "Available"

  def get_title(self):
    return self.__title
  
  def get_author(self):
    return self.__author
  
  def get_isbn(self):
    return self.__isbn
  
  def get_genre(self):
    return self.__genre
  
  def get_publication_date(self):
    return self.__publication_date
  
  def borrow_book(self):
    if self.availability_status == "Available":
      self.availability_status = "Unavailable"
      return True
    return False

  def return_book(self):
    self.availability_status = "Available" 

  def view_book(self):
    print(f"\nTitle: {self.get_title()} Author: {self.get_author()}\nBook Number: {self.get_isbn()}\nGenre: {self.get_genre()}\nPublished: {self.get_publication_date()}\nAvailability: {self.availability_status}")

class FictionBook(Book):
  def __init__ (self,title, author, isbn, genre, publication_date):
    super().__init__(title, author, isbn, genre, publication_date)

class NonFictionBook(Book):
  def __init__ (self,title, author, isbn, genre, publication_date):
    super().__init__(title, author, isbn, genre, publication_date)

class BiographyBook(Book):
  def __init__ (self,title, author, isbn, genre, publication_date):
    super().__init__(title, author, isbn, genre, publication_date)

class SelfHelpBook(Book):
  def __init__ (self,title, author, isbn, genre, publication_date):
    super().__init__(title, author, isbn, genre, publication_date)

class MysteryBook(Book):
  def __init__ (self,title, author, isbn, genre, publication_date):
    super().__init__(title, author, isbn, genre, publication_date)

class ScienceFictionBook(Book):
  def __init__ (self,title, author, isbn, genre, publication_date):
    super().__init__(title, author, isbn, genre, publication_date)

class ThrillersBook(Book):
  def __init__ (self,title, author, isbn, genre, publication_date):
    super().__init__(title, author, isbn, genre, publication_date)



class User:
  def __init__ (self,user_name,library_id):
    self._user_name = user_name
    self._library_id =library_id
    self._borrowed_books = []

  def get_user_name(self):
    return self._user_name
  
  def get_library_id(self):
    return self._library_id
  
  def get_borrowed_books(self):
    return self._borrowed_books
  
  def adding_borrowed_books(self,book):
    if book in self.get_borrowed_books():
      print(f"{book} is already loaned to {self.get_user_name()}")
    else:
      self.get_borrowed_books().append(book)
      print(f"'{self.get_user_name()}' has checked out '{book}'")

  def returning_borrowed_book(self,book):
    if book in self.get_borrowed_books():
      self.get_borrowed_books().remove(book)
      print(f"'{book}' has been checked back in")
    else:
      print(f"'{book}' is not checked out to '{self.get_user_name()}'")

  def view_user_details(self):
    print(f"{self.get_user_name()} User I.D. Number: {self.get_library_id()}\nBorrowed Books: {self.get_borrowed_books()}")

class Author:
  def __init__ (self, author_name, biography):
    self.author_name = author_name
    self.biography = biography
  #Author: A class representing book authors with attributes like name and biography.
  def view_author_details(self):
    print(f"{self.author_name}\nBiography:\n{self.biography}")

class Genre:
  def __init__(self,genre_name,description,category):
    self.genre_name = genre_name
    self.description = description
    self.category = category

  def view_genre_details(self):
    print(f"{self.genre_name}:\nDescription-{self.description}\nCategory: {self.category}")

class UserInterface:
  def __init__ (self):
    self.book_inventory = {}
    self.user_information = {}
    self.author_information = {}
    self.genre_information = {}
    self.current_loans = {}

  def book_operations(self):
    while True:
      book_file = FileHandling.opening_book_file("library_Management_System\\book_inventory.txt",self.book_inventory)
      current_loans_file = FileHandling.open_current_loans_file("Library_Management_System\\current_loans.txt",self.current_loans)
      user_file = FileHandling.opening_user_file("library_Management_System\\library_users.txt",self.user_information)
      print("\nBook Operations Menu:\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books\n6. Exit")
      book_operation_choice = input("Please choose a menu option: ")
      if book_operation_choice == "1":
        Adding_information.add_book(book_file)
      elif book_operation_choice == "2":
        BookProcessing.checking_book_out(book_file, user_file, current_loans_file)
      elif book_operation_choice == "3":
        BookProcessing.returning_book(book_file, user_file, current_loans_file)
      elif book_operation_choice == "4":
        book_search = input("Enter book name to search: ").title()
        if book_search in book_file:
          Book.view_book(book_file[book_search])
        else:
          print("Book Not Found")
      elif book_operation_choice == "5":
        for info in book_file.values():
          Book.view_book(info)
        pass
      elif book_operation_choice == "6":
        print("Returning to Main Menu...")
        break
      else:
        print("Invalid Choice")
      FileHandling.export_book_file("library_Management_System\\book_inventory.txt",self.book_inventory)
      FileHandling.exporting_current_loans_file("Library_Management_System\\current_loans.txt",self.current_loans)
      FileHandling.exporting_user_file("library_Management_System\\library_users.txt",self.user_information)

  def user_operations(self):
    while True:
      user_file = FileHandling.opening_user_file("library_Management_System\\library_users.txt",self.user_information)
      print("\nUser Operations Menu:\n1. Add a new user\n2. View user details\n3. Display all users\n4. Exit")
      user_operation_choice = input("Please choose a menu option: ")
      if user_operation_choice == "1":
        Adding_information.add_user(user_file)
      elif user_operation_choice == "2":
        users_name = input("Enter Username: ").title()
        if users_name not in user_file:
          print(f"{users_name} not found in User Data Base")
        else:
          User.view_user_details(user_file[users_name])
      elif user_operation_choice == "3":
        for user, user_info in user_file.items():
          User.view_user_details(user_info)
      elif user_operation_choice == "4":
        print("Returning to Main Menu...")
        break
      else:
        print("Invalid Choice")
      FileHandling.exporting_user_file("library_Management_System\\library_users.txt",self.user_information)
      
  def author_operations(self):
    while True:
      author_file = FileHandling.opening_author_file("library_Management_System\\authors.txt",self.author_information)
      print("\nAuthor Operations:\n1. Add a new author\n2. View author details\n3. Display all authors\n4. Exit")
      author_operation_choice = input("Please choose a menu option: ")
      if author_operation_choice == "1":
        Adding_information.add_author(author_file)
      elif author_operation_choice == "2":
        author_name = input("Enter Authors name: ").title()
        if author_name not in author_file:
          print(f"{author_name} not found in Author Data Base")
        else:
          Author.view_author_details(author_file[author_name])
      elif author_operation_choice == "3":
        for author, author_info in author_file.items():
          Author.view_author_details(author_info)
      elif author_operation_choice == "4":
        print("Returning to Main Menu...")
        break
      else:
        print("Invalid Choice")
      FileHandling.exporting_author_file("library_Management_System\\authors.txt",self.author_information)

  def genre_operations(self):
    while True:
      genres_file = FileHandling.opening_genres_file("library_Management_System\\genres.txt",self.genre_information)
      print("\nGenre Operations:\n1. Add a new genre\n2. View genre details\n3. Display all genres\n4. Exit")
      genre_operation_choice = input("Please choose a menu option: ")
      if genre_operation_choice == "1":
        Adding_information.add_genre(genres_file)
        pass
      elif genre_operation_choice == "2":
        genre_name = input("Enter Genre: ").title()
        if genre_name not in genres_file:
          print(f"{genre_name} not found in Genre Data Base")
        else:
          Genre.view_genre_details(genres_file[genre_name])
        pass
      elif genre_operation_choice == "3":
        for genre, genre_info in genres_file.items():
          Genre.view_genre_details(genre_info)
        pass
      elif genre_operation_choice == "4":
        print("Returning to Main Menu...")
        break
      else:
        print("Invalid Choice")
      FileHandling.exporting_genres_file("library_Management_System\\genres.txt",self.genre_information)

class FileHandling:

  def export_book_file(book_file,changed_book_file):
    try:
      with open(book_file, 'w') as file:
        for book, book_info in changed_book_file.items():
          file.write(f"{book_info.get_title()},{book_info.get_author()},{int(book_info.get_isbn())},{book_info.get_genre()},{book_info.get_publication_date()},{book_info.availability_status}\n")
    except FileNotFoundError:
      print("Not Saved")
    except AttributeError:
      print("Not Saved")

  def opening_book_file(book_file,book_inventory):
    try:
      with open(book_file, "r") as file:
        for line in file:
          title, author, isbn, genre, publication_date, availability = line.strip().split(',')
          book = Book(title,author,int(isbn),genre,publication_date)
          book.availability_status = availability
          book_inventory[title] = book
        return book_inventory
    except AttributeError:
      pass

  def exporting_user_file(user_file,changed_user_file):
    try:
      with open(user_file, 'w') as file:
        for user_info in changed_user_file.values():
          file.write(f"{user_info.get_user_name()}/{int(user_info.get_library_id())}/{','.join(user_info.get_borrowed_books())}\n")
          print("user file saved")
    except FileNotFoundError:
      print("User File Not Saved")
    except AttributeError:
      print("User File Not Saved")

  def opening_user_file(user_file,user_information):
    try:
      with open(user_file, "r") as file:
        for line in file:
          user_name,library_id,borrowed_books = line.strip().split('/')
          user =  User(user_name,int(library_id))
          user._borrowed_books = borrowed_books.split(",")
          user_information[user_name] = user
        return user_information
    except AttributeError:
      pass
    
  def exporting_author_file(author_file,changed_author_file):
    try:
      with open(author_file, 'w') as file:
        for author, author_info in changed_author_file.items():
          file.write(f"{author_info.author_name}/{int(author_info.biography)}\n")
    except FileNotFoundError:
      print("Not Saved")
    except AttributeError:
      print("Not Saved")

  def opening_author_file(author_file,author_information):
    try:
      with open(author_file, "r") as file:
        for line in file:
          author_name, biography = line.strip().split('/')
          author_information[author_name] = Author(author_name,biography)
        return author_information
    except AttributeError:
      pass

  def exporting_genres_file(genres_file,changed_genres_file):
    try:
      with open(genres_file, 'w') as file:
        for genre, genre_info in changed_genres_file.items():
          file.write(f"{genre_info.genre_name()},{genre_info.description},{genre_info.category}\n")
    except FileNotFoundError:
      print("Not Saved")
    except AttributeError:
      print("Not Saved")

  def opening_genres_file(genres_file,genre_information):
    try:
      with open(genres_file, "r") as file:
        for line in file:
          book_name,description,category = line.strip().split(',')
          genre_information[book_name] = Genre(book_name,description,category)
        return genre_information
    except AttributeError:
      pass

  def exporting_current_loans_file(current_loans_file,changed_current_loans_file):
    try:
      with open(current_loans_file, 'w') as file:
        for book_on_loan, person_loaning_book in changed_current_loans_file.items():
          file.write(f"{book_on_loan},{person_loaning_book}\n")
    except FileNotFoundError:
      print("Not Saved")
    except AttributeError:
      print("Not Saved")

  def open_current_loans_file(current_loans_file,current_loans):
    try:
      with open(current_loans_file, "r") as file:
        for line in file:
          book_title,person_borrowing_book = line.strip().split(',')
          current_loans[book_title] = person_borrowing_book
        return current_loans
    except AttributeError:
      pass

class Adding_information:
  def users_name_authenticator(user_name):
    users_name_standard = r"^\w{2,15}\s\w{2,15}$"
    matching_users_name = re.match(users_name_standard,user_name)
    if matching_users_name:
      return True
    else:
      return False

  def add_book(book_file):
    try:
      title = input("Enter Title of book: ").title()
      if title not in book_file:
        author = input("Enter Author of book: ").title()
        isbn = int(input("Enter ISBN: "))
        genre = input("Enter Genre of book: ").title()
        publication_date = input("Enter Publication Date [YYYY-MM-DD]: ").title()
        book_file[title] = Book(title, author, isbn, genre, publication_date)
      else:
        print(f"{title} is already in Book Database")
        
    except ValueError:
      print("Enter a 'Number' for the ISBN")

  def add_user(user_file):
    try:
      user_name = input("Enter Name of user to be added: ").title()
      if Adding_information.users_name_authenticator(user_name):
        if user_name not in user_file:
          library_id = int(input("Enter Library I.D. Number: "))
          user_file[user_name] = User(user_name,library_id)
        else:
          print(f"{user_name} is already in User Database")
    except ValueError:
      print("Enter a 'Number' for the Library I.D.")

  def add_author(author_file):
    author_name = input("Enter Name of Author to be added: ").title()
    if author_name not in author_file:
      biography = input("Enter biography for Author: ")
      author_file[author_name] = Author(author_name, biography)
    else:
      print(f"{author_name} is already in Author Data Base")

  def add_genre(genre_file):
    genre_name = input("Enter Genre: ").title()
    if genre_name not in genre_file:
      description = input("Enter Description of Genre: ").title()
      category = input("Enter Genre Category: ").title()
      genre_file[genre_name] = Genre(genre_name,description,category)
    else:
      print(f"{genre_name} is already in Genre Data Base")

class BookProcessing:

  def checking_book_out(book_file,user_information,current_loans):
    user_search = input("Enter in User checking out book: ").title()
    book_search = input("Enter book name to Borrow: ").title()
    if book_search in book_file and user_search in user_information:
      if book_file[book_search].borrow_book():
        current_loans[book_search] = user_search
        user_information[user_search].adding_borrowed_books(book_search)
      else:
        print(f"'{book_search}' is already Checked Out")
    else:
      print(f"'{book_search}' is not in Library Data Base or '{user_search}' is not in Library Data Base")

  def returning_book(book_file,user_information,current_loans):
    user_returning_book = input("Enter Person Returning Book: ").title()
    book_return = input("Enter Book being returned: ").title()
    if book_return in current_loans and book_return in book_file and user_returning_book in user_information:
      book_file[book_return].return_book()
      user_information[user_returning_book].returning_borrowed_book(book_return)
      del current_loans[book_return]
    else:
      print(f"'{book_return}' is not checked out or '{user_returning_book}' is not in Library Data Base")