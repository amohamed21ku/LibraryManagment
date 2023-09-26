from LibraryItem import LibraryItem
from Books import Books
from DVD import DVD
from Customer import Customer

def display_menu():
    print("\nMain Menu:")
    print("1. Take an Item")
    print("2. Return an Item")
    print("3. Add a book")
    print("4. Exit")

def display_available_items():
    with open("Items.txt", "r") as file:
        items = file.readlines()
        if not items:
            print("No books available at the moment.")
            return
        print("Available Items:")
        for index, item in enumerate(items, start=1):
            print(f"{index}. {item.strip()}")


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
        print(f"Item with NAME '{TITLE}' has been removed.")
    else:
        print(f"Item with NAME '{TITLE}' not found.")



#*****************************************************************************************


members = []
Items = []
def refresh_users():
    members = []
    with open("members.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            member_id, name, age = data
            customer = Customer(member_id, name, age)
            members.append(customer)
    return members
members = refresh_users()

def refresh_Items():
    Items = []
    with open("Items.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            title,author,Item_id,isbn = data
            book = Books(title, author, Item_id,isbn)
            book.add_book
            Items.append(book)
    return Items
Items = refresh_Items()

# Function to generate a unique member ID
def generate_id(member_number,pre):
    return f"{pre}{str(member_number).zfill(3)}"


# Check if the user is a new or existing member

while True:
    num_rows = 5  
    num_columns = 40

    max_asterisks = 2 * num_columns - 1

    # Print the pyramid
    for i in range(1, num_rows + 1):
        num_asterisks = 2 * i - 1
        num_spaces = (max_asterisks - num_asterisks) // 2
        print(" " * num_spaces, end="")
        print("*" * num_asterisks)




    print("****************************Welcome to the library!*************************************\n")
    current_user = None
    choice = input("Are you a new member? (yes/no): ").lower()
    
    if choice == "yes":
        # If the user is a new member, collect their name and age
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        
        # Generate a new member ID based on the number of existing members
        with open("members.txt", "r") as file:
            lines = file.readlines()
            member_number = len(lines) + 1
            member_id = generate_id(member_number,"M")
        
        # Store the new member's information in the text file
        with open("members.txt", "a") as file:
            file.write(f"{member_id},{name},{age}\n")
        
        print(f"Welcome, {name}! Your member ID is {member_id}")
        members = refresh_users()
        current_user = members[-1]

        break
    
    elif choice == "no":
        # If the user is an existing member, read their information from the text file
        member_id = input("Enter your member ID: ")
        for customer in members:
            if(customer.customer_id == member_id):
                current_user = customer
                print(f"Welcome back {current_user.name}")
                break 
        if(current_user == None):
            print("Member ID not found. Please try again.")       
        break
    
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

while True:
    display_menu()
    option = input("Select an option (1/2/3/4): ")


    if option == "1":
        # Take a book
        display_available_items()
        if Items:
            try:
                choice = int(input("Enter the book you want to take, choose by index: "))
                if 1 <= choice <= len(Items):
                    if current_user is not None:
                        Items = refresh_Items()
                        current_user.take_item(Items[choice-1])
                        remove_item(Items[choice-1 ].title)
                        Items.remove(Items[choice-1 ])
                    else:
                        print("Please log in or create an account before taking an item.")
                else:
                    print("Invalid choice. Please choose a valid index.")
            except ValueError:
                print("Invalid input. Please enter a valid index.")

    elif option == "2":
        # Return a book
        if current_user is not None:
            current_user.display_taken_items()
            if current_user.taken_items:
                try:

                    returned_book_index = int(input("Which item you want to return, choose by index: "))
                    title = current_user.taken_items[returned_book_index - 1].title
                    author = current_user.taken_items[returned_book_index - 1].author
                    isbn = current_user.taken_items[returned_book_index - 1].isbn

                    if 1 <= returned_book_index <= len(current_user.taken_items):
                        current_user.return_item(current_user.taken_items[returned_book_index - 1])


                        with open("Items.txt", "r") as file:
                            lines = file.readlines()
                            item_number = len(lines) + 1
                            item_id = generate_id(item_number,"B")
                            Items.append(Books(title,author,item_id,isbn).add_book())
                    else:
                        print("Invalid choice. Please choose a valid index.")
                except ValueError:
                    print("Invalid input. Please enter a valid index.")
            else:
                print("You haven't borrowed any items yet.")
        

    elif option =="3":
        title = input("Enter the title of the book you want to Add: ").strip()
        author = input("Enter the author : ").strip()
        isbn = input("Enter the isbn: ").strip()
        with open("Items.txt", "r") as file:
            lines = file.readlines()
            item_number = len(lines) + 1
            item_id = generate_id(item_number,"B")
            Items.append(Books(title,author,item_id,isbn).add_book())
            refresh_Items()

    elif option =="4":
        break
    
    else:
        print("Invalid option. Please select a valid option (1/2/3).")

print("Thank you")








    
   
   


