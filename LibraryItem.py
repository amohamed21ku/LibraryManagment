from abc import ABC, abstractmethod

class LibraryItem(ABC):
    items_in_lib = []
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.istaken = False
        
        

    @abstractmethod
    def info(self):
        pass

    def remove_item(TITLE):
        with open("Items.txt", "r") as file:
            lines = file.readlines()

        found = False
        with open("Items.txt", "w") as file:
            for line in lines:
                data = line.strip().split(',')
                if data[0].strip() == TITLE:
                    found = True
                else:
                    file.write(line)

        if found:
            print(f"Item with ID '{TITLE}' has been removed.")
        else:
            print(f"Item with ID '{TITLE}' not found.")




    def take(self,customer):
        if not self.istaken:
            self.istaken = True
            print(f"{self.title} by {self.author} is taken by {customer.name}.")
            # self.remove_item(self.title)
        else:
            print(f"{self.title} by {self.author} is already taken.")

    def Return(self):
        if self.istaken:
            self.istaken = False
            print(f"{self.title} by {self.author} is returned.")

        else:
            print(f"{self.title} by {self.author} is already returned.")