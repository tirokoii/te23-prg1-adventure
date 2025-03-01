## Vad har jag gjort?

- En meny
- Loot system - ish (Inte riktigt klar)
- History
- Restart, Quit och continue i menyn

### Hur?
Abslout ingen aning (det funkar typ ändå)

#### Meny
- En funktion som checkar om man har skrivit en siffra eller m (för menu)
- En funktion med som printar och checkar input av användaren för att se att använadren skrivit in rätt
##### Och hur i hela friden har jag skrivit det?
Så här:

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
            choice = page_history(pages)
            return choice
        else:
            print("Please write a number between 1-4")

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



        
