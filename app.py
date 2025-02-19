# from book import BOOK
from robosquirrels import ROBOSQUIRRELS
game = True

def menu(choice):
    while True:
        print("Quit: 1")
        print("Restart: 2")
        print("Continue: 3")
        choice = input_int("Choose: ")
        if choice == 1:
            return False
        elif choice == 2:
            return "Restart"
        elif choice == 3:
            return True
        else:
            print("Nice")
        

def input_int(prompt): #Fixes ValueError syntax
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def input_check(prompt):
    while True:
        choice = input(prompt)
        if choice.lower() == "m":
            game = menu(choice)
            return game #Work on menu
        elif choice.isalpha():
            print("Invalid input. Please write a number or m for menu")
        elif choice.isdigit():
            choice = int(choice)
            return choice
        else:
            print("Invalid input. Please write a number or m for menu")

def get_page(book_data, page_id): #Gets the book ids
    for page in book_data:
        if page["id"] == page_id:
            return page
    return None

def show_page(page): #Prints the page
    print(page["title"])
    print(page["text"])
    for i, option in enumerate(page["options"]):
        print(f"{i + 1}. {option['text']}")


def main(): #Makes everything work
    game = True
    current_id = 1
    inventory = []
    while True and current_id is not None and game == True or game == "Restart":
        if game == "Restart":
            current_id = 1
        game = True
        current_page = get_page(ROBOSQUIRRELS, current_id)
        show_page(current_page)
        if "loot" in current_page:
            print(f"You found {current_page['loot']}!")
            inventory.append(current_page["loot"])
    
        choice = input_check("Enter your choice: ")
        if choice == False:
            game = False
        elif choice == "Restart":
            game = "Restart"
        elif choice == True:
            game = True
        elif 1 <= choice <= len(current_page["options"]):
            current_id = current_page["options"][choice - 1]["next_id"]
        else:
            print("Invalid choice. Please try again.\n")
            current_id = current_id


if __name__ == "__main__":   
    main()
