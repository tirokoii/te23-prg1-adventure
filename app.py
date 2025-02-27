# from book import BOOK
from robosquirrels import ROBOSQUIRRELS
game = True

#Spara en historik över användarens val och låta dem gå tillbaka till tidigare sidor. Tips: använd en lista för att spara historiken, du lägger till spelarens val i listan med append.
#Skapa en replay-funktion som spelar upp berättelsen från historiken.

def page_history(pages):
    for page_number in pages:
        for page in ROBOSQUIRRELS:
            if page["id"] == page_number:
                print(f"{page_number}. {page["title"]}")
                break
    while True:
        choice = input_int("Which page do you wish to jump to? ")
        print("\n")
        if choice in pages:
            return choice
        else:
            print("You haven't discovered that page yet")


def menu(choice, pages):
    while True:
        print("Quit: 1")
        print("Restart: 2")
        print("Continue: 3")
        print("Pages: 4")
        choice = input_int("Choose: ")
        print("\n")
        if choice == 1:
            return False
        elif choice == 2:
            return "Restart"
        elif choice == 3:
            return "continue"
        elif choice == 4:
            current_id = page_history(pages)
            return current_id
        else:
            print("Please write a number between 1-4")
        

def input_int(prompt): #Fixes ValueError syntax
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def input_check(prompt, pages): #Menu choice
    while True:
        choice = input(prompt)
        if choice.lower() == "m":
            game = menu(choice, pages)
            return game
        elif choice.isalpha():
            print("Invalid input. Please write a number or m for menu")
        elif choice.isdigit():
            choice = int(choice)
            return choice
        else:
            print("Invalid input. Please write a number or m for menu")

def get_page(book_data, page_id): #Gets the book id, book_data(book pages) and compares the id
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
    history_list = []
    while True and current_id is not None and game == True or game == "Restart":
        if game == "Restart":
            current_id = 1
        game = True
        while True:
            current_page = get_page(ROBOSQUIRRELS, current_id)
            show_page(current_page)
            if current_id not in history_list:
                history_list.append(current_id)
                history_list.sort()

            if "loot" in current_page:
                print(f"You found {current_page['loot']}!")
                inventory.append(current_page["loot"])
        
            choice = input_check("Enter your choice: ", history_list)
            if choice in history_list:
                current_id = choice
            else:
                break

        if choice == False:
            game = False
        elif choice == "Restart":
            game = "Restart"
        elif choice == "continue":
            game = True
        elif 1 <= choice <= len(current_page["options"]):
            current_id = current_page["options"][choice - 1]["next_id"]
            if current_id > 18:
                print("Thank you for playing!")
                break
        else:
            print("Invalid choice. Please try again.\n")
            current_id = current_id


if __name__ == "__main__":   
    main()
