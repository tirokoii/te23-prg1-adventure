## Vad har jag gjort?

- En meny
- Restart, Quit och continue i menyn
- Historik - (typ klar)
- Loot system - ish (Inte riktigt klar)

### Hur?
Abslout ingen aning (det funkar typ)

#### Meny
- En funktion som checkar om man har skrivit en siffra eller m (för menu)
- En funktion med som printar och checkar input av användaren för att se att användaren skrivit in rätt

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


##### Hur fungerar det?
Menyn fungerar så att den loopas tills man skrivit in rätt. Den printar själva menyn och låter användaren skriva in en siffra, eftersom jag har använt jensadevs handy-dandy input check, behöver jag inte ens förklara hur input_int fungerar. Den checkar bara så att inputen är en siffra, om inte får man skriva om det. Om choice är == någon av siffrorna som menyn bygger på kommer den att göra en av 4 saker. 

Returnera False, "restart", continue eller, starta page_history funktionen. 

När den returnera False kommer spelet att avslutas, och "restart" kommer den att starta om speler, om continue fortsätter den bara och sist om page_history kommer den öppna menyn för att välja pages man redan har gått till. Simpelt. Eller?

Jahopp, men hur fungerar input checken då? Jo den inehåller också en while loop, så att om man skriver fel kommer den att börja om. Den har också en input men istället för att den är som jensadev's, som checkar om value error, så använderden if-satser (villkor). Då kan det hända en av 4 saker, om choice är "m" kommer den att sätta game = menu, vilket startar menu funktionen. Det är på denna som det returnerade värdet från menu() funktion kommer spela roll. Om input:en är en string som är en bokstav så kommer den att ge ett felmeddelande, tvärtom är input:en en string som är ett tal kommer den att returnera inputens värde. Sist och minst om den inte är något av dessa (vilket är otroligt) kommer den att skriva ett fel meddelande till användaren. Fantastiskt att du orkar läsa igenom detta, bara "lite" till kvar nu...

#### Historik
- En list som sparar historik över vilka pages man besökt tidigare

##### Hur ser det ut?

Precis så här:

history_list = []

if current_id not in history_list:

                history_list.append(current_id)

                history_list.sort()

def page_history(pages):

    for page_number in pages:

        for page in ROBOSQUIRRELS:

            if page["id"] == page_number:

                print(f"{page_number}. {page["title"]}")'

                break

    while True:

        choice = input_int("Which page do you wish to jump to? ")

        print("\n")

        if choice in pages:

            choice = [choice, "p"]

            return choice 

        else:

            print("You haven't discovered that page yet")

if type(choice) == int:

                choice = choice

            elif "p" in choice:

                current_id = choice[0]

                choice = current_id


##### Hur går det till?

Genom att skriva i ett py dokument (jokes aside)

Det finns en tom lista som kan fyllas.

När villkoret möts, i detta fall när current_id inte finns i listan, så kommer den sidans id som man är på att läggas till. Om det finns flera värden i listan kommer sort() metoden att sortera dem efter minst till störst.

Den delen där history listen kommer användas är page_history() funktionen (den är läskig, rikitgt läskig).

Den har en for loop i en foor loop i sig som är beroande av listan history, där jag har valt att namnge den pages istället. Då för varje sidas nummer i listan kommer den att för varje sida i ROBOSQUIRRELS dokumentet, att kolla om sidans id matchar med listans siffra. Om det matchar skriver den ut siffran och dess titel samt "breakar" den första for loopen.
Sedan finns en while loop efter det. Den innehåller en input (input_int) och villkor. Om input:en är i pages så kommer den att returnera, input:ens värde och "p" i en lista (Det kommer senare användas för att byta till den sidan i en if sats, i main funktionen). 
Om inte så kommer den att ge ett fel meddelande (Jag har inte gjort en funktion som man kan gå ut därifrån (Men å-andra sidan är det inte nödvändigt)). 
Sedan i main funktionen finns det en if-sats som har villkoret om choice är en int(en siffra, som inte är string) kommer den att sätta siffran som siffran (jag vet konsigt, kom inte på något bättre), inget kommer hända. Men om det returnerade värdet av input:en har ett "p" i sig kommer den att sätta current_id till den sidan man valt (siffran). Nu har du bara loot systemet kvar, lycka till!

#### Loot system
- Ett loot system, där spelaren/användaren kan få och använda loot
##### Hur ser det ut?
Ungefär på detta viss:

inventory = []

if "loot" in current_page and "loot" not in inventory and len(current_page["loot"]) > 0:

    while True:

        print(f"You found {current_page['loot']}!")

        loot_list = current_page["loot"]

        for item in loot_list:  

            inventory.append(item)

        break

I robosquirrels dokumentet:

"loot": ["Rebel Medkit", "Squirrel Credits", "Power Cell"],


##### Vad händer?

Jaha, då var det dags att skriva hur det fungerar också...

Ja-ja, det börjar med den if-satsen som jag så snällt fått av jensadev. Den fungerar på så viss att om en "loot" key finns i robosquirrels och loot:en inte redan finns i inventory samt "loot" list längden är över 0 i robosquirrels, kommer den att starta en while loop. Loot:en som finns på den sidan kommer då skrivas ut och den loot:en kommer sparas i en lista. I for loop:en som kommer efter blir listan använd för att ta ut loot separat från listan och spara dem i inventory. Till sist kommer while loopen att avslutas när for loop:en är klar.

"loot" är en key som finns i varje sida i robosquirrels och har up till 3 värden.

Men jag har inte hunnit göra så att man inte kan välja de alternativ som kräver loot ännu, eller gjort så att loot:en försvinner "för evigt" om man försöker återvända till en sida senare med page_history funktionen.

Jag såg nyss att man skulle skriva kort(Whoopsie)





