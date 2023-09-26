from LibraryItem import LibraryItem

class Books(LibraryItem):
    
    def __init__(self, title, author, item_id, isbn):
        super().__init__(title, author, item_id)
        self.isbn = isbn

    def add_book(self):
          with open("Items.txt", "a") as file:
            file.write(f"{self.title},{self.author},{self.item_id},{self.isbn}\n")

          

       
        

    def info(self):
        print(f"Book Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Item ID: {self.item_id}")
        if self.istaken:
            print("Status: Taken")
        else:
            print("Status: Available")
