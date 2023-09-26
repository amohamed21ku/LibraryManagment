from LibraryItem import LibraryItem
class Customer:
    def __init__(self, customer_id, name,age):
        self.customer_id = customer_id
        self.name = name
        self.age = age
        self.taken_items = []

    def take_item(self, library_item):
        library_item.take(self)
        self.taken_items.append(library_item)
    
           

    def return_item(self, library_item):
        if library_item in self.taken_items:
            library_item.Return()
            self.taken_items.remove(library_item)
       
        else:
            print("You don't have this item.")

    def display_taken_items(self):
        if self.taken_items == []:
            print("You haven't taken out any items.")
        else:
            print(f"{self.name}'s taken Items:")
            index = 1
            for item in self.taken_items:
                print(f"{index}.")
                item.info()
                print("")
                index=+1

    