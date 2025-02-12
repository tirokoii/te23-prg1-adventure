# from book import BOOK
from robosquirrels import ROBOSQUIRRELS

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_page(book_data, page_id):
    for page in book_data:
        if page["id"] == page_id:
            return page
    return None

def show_page(page):
    print(page["title"])
    print(page["text"])
    for i, option in enumerate(page["options"]):
        print(f"{i + 1}. {option['text']}")


def main():
    current_id = 1
    inventory = []
    while True and current_id is not None:
        current_page = get_page(ROBOSQUIRRELS, current_id)
        show_page(current_page)
        if "loot" in current_page:
            print(f"You found {current_page['loot']}!")
            inventory.append(current_page["loot"])
        choice = input_int("Enter your choice: ")
        if 1 <= choice <= len(current_page["options"]):
            current_id = current_page["options"][choice - 1]["next_id"]
        else:
            print("Invalid choice. Please try again.")
            current_id = None


if __name__ == "__main__":
    main()
