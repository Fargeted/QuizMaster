import random
import time

class Person:
    def __init__(self, namn, ålder, kön):
        self.__namn = namn
        self.__ålder = ålder
        self.__kön = kön
    
    def get_namn(self):
        return self.__namn 
    
    def set_namn(self, namn):
        self.__namn = namn

    def get_ålder(self):
        return self.__ålder 
    
    def set_ålder(self, ålder):
        self.__ålder = ålder

    def get_kön(self):
        return self.__kön 
    
    def set_kön(self, kön):
        self.__namn = kön

class Frågor:
    def __init__(self, kategori, fråga_text, rätt_svar, fel_svar):
        self.__kategori = kategori #Vilken kategori frågan tillhör till
        self.__fråga_text = fråga_text # Vad frågan är t.ex. "vad är 2+2"
        self.__rätt_svar = rätt_svar # Används för att spara rätt fråga
        self.__fel_svar = fel_svar # Används för att spara de fela frågor
    
    def get_kategori(self):
        return self.__kategori
    
    def set_kategori(self, kategori):
        self.__kategori = kategori
    
    def get_fråga_text(self):
        return self.__fråga_text
    
    def set_fråga_text(self, fråga_text):
        self.__fråga_text = fråga_text
    
    def get_rätt_svar(self):
        return self.__rätt_svar
    
    def set_rätt_svar(self, rätt_svar):
        self.__rätt_svar = rätt_svar
    
    def get_fel_svar(self):
        return self.__fel_svar
    
    def set_fel_svar(self, fel_svar):
        self.__fel_svar = fel_svar

    def ställ_fråga(self):
        print(f"\nKategori: {self.__kategori}")
        print(f'\n"{self.__fråga_text}"\n')

        alternativ = self.__fel_svar + [self.__rätt_svar] # lägger till den "rätta svaret" i listan som är "fel svar"
        random.shuffle(alternativ) # ändrar på ordningen av listans frågor så att den rätta svaret ligger inte på samma plats varje gång

        for i, alt in enumerate(alternativ): # I börjar leta runt i varje index av listan. Alltså börjar den på 0 och slutar på 3. Alt kollar också inom index fast hämtar själva indexets str värde
            print(f"{i+1}. {alt}") # I är adderad med 1 så att listan visar "1. (alt) 2. (alt) 3. (alt) 4. (alt)", Enumarate används för att hämta både index värde (platsnummer) och värde (datatyp)

        try:
            val = int(input("\n|Ditt svar 1-4|: "))
            if alternativ[val-1] == self.__rätt_svar: #listan har en värde från 0 - 3 och alternativen visar 1 - 4, därför måste svaret minskas med 1 för att kontrollera att svaret var rätt
                print("Korrekt!")
                return True
            else:
                print(f"Fel! Rätt svar var: {self.__rätt_svar}")
                return False
        
        except:
            print("Du behöver välja en svar mellan 1 - 4")
            print("Dock så räknas det som ett svar så tyvärr förlorar du ett liv")
            print(f"Btw, rätt svar var: {self.__rätt_svar}")
            return False
            

#FUNKTIONER
def hämta_person_info(gubbe): # Hämtar allt information om användaren ifall det behövs
    return gubbe.get_namn(), gubbe.get_ålder(), gubbe.get_kön()

def hämta_fråga(fråga): #hämtar frågor och printar det lik hämta_person_info() funktionen ovanför
    return fråga.get_kategori(), fråga.get_fråga_text(), fråga.get_rätt_svar(), fråga.get_fel_svar() 

def checkpoint(svar, verifikation):
    print(f"\nVänta nu, du har nått en checkpoint!\nSå ja {användare.get_namn()}, Du har nu nått {poäng} poäng och fått {svar} frågor rätt!")
    print(f"Eftersom du har nu fått {svar} frågor rätt så har du valet att antingen sluta nu, vinna och ta med dig alla dina poäng.")
    print(f"Eller så kan du fortsätta vidare och få 25% mer poäng för varje fråga du får rätt! \nDetta multiplikator även byggs på ifall du når nästa checkpoint!")
    print(f"\nSå, vill du lämna eller stanna, {användare.get_namn()}?")

    while True:
        try:
            val = int(input("|1 = lämna|\n|2 = stanna|\n"))
            if val == 1:
                print("Så ledsen att höra det, hoppas vi ses igen snart!\n")
                verifikation = False
                break
            elif val == 2:
                print("\nDå så fortsätter vi!\n(Du får nu 25% mer poäng för varje fråga du får rätt)")
                verifikation = True
                break
            else: #Extra felhantering ifall användaren skriver en siffra som inte är 1 eller 2
                print("\nSnälla skriv en siffra mellan 1 och 2")
                continue
        except ValueError:
            print("\nDu behöver skriva ner antingen 1 eller 2. \n1 betyder du lämnar och vinner med dina poäng\n2 betyder du stannar och spelet fortsätter vidare\n")
            continue

    return verifikation 

def highscore(poäng, rätt_svar, fel_svar, counter):
    print(f"\n|Highscore: {poäng}\n|Antal rätt svar: {rätt_svar}\n|Antal fel svar: {fel_svar}\n|Antal frågor ställt: {counter}")
    return

def hantera_checkpoint(verifikation, multiplier, rätt_svar, poäng, fel_svar, counter):
    if rätt_svar % 5 == 0 and rätt_svar // 5 > verifikation: #rätt_svar % 5 == 0 kollar om antalet rätt svar är en antal av 5 t.ex. 5, 10, 15, 20 osv.
        # rätt_svar // 5 > verifikation säkerställer att checkpointen triggar bara ett gång, t.ex. när rätt svar går från 4-5 och inte varje gång användaren har 5.
        verifikation = checkpoint(rätt_svar, verifikation)
        if verifikation == False:
            highscore(poäng, rätt_svar, fel_svar, counter)
            quit()
        elif verifikation == True:
            multiplier += 0.25
            verifikation = rätt_svar // 5 # uppdaterar till checkpoint nivå, 5 = 1, 10 = 2 osv.
    return verifikation, multiplier

#FRÅGOR
frågedata = { 
    "vetenskap": [ #listor används för att enklare kunna sortera mellan kategoriers frågor och gör det enklare att lägga till flera frågor i framtiden och vilken kategori användaren vill svara.
        {"fråga": "Vad heter den största planet i vårt solsystem?", "rätt": "Jupiter", "fel": ["Saturnus", "Mars", "Jorden"]},
        {"fråga": "Vilket grundämne har kemiska beteckningen O?", "rätt": "Syre", "fel": ["Väte", "Kväve", "Kol"]},
        {"fråga": "Hur många ben har en vuxen människa normalt?", "rätt": "206", "fel": ["207", "201", "212"]},
        {"fråga": "Vad kallas den process där växter omvandlar solljus till energi?", "rätt": "Fotosyntes", "fel": ["Förbränning", "Cellandning", "Fermentering"]},
        {"fråga": "Vilken vetenskapsmän formulerade gravitationslagen?", "rätt": "Isaac Newton", "fel": ["Albert Einstein", "Galileo Galilei", "Nikola Tesla"]}
    ],
    "matematik": [
        {"fråga": "Vad är 7 x 8?", "rätt": "56", "fel": ["54", "67", "49"]},
        {"fråga": "Vad är roten ur 144?", "rätt": "12", "fel": ["14", "11", "8"]},
        {"fråga": "Hur många grader är en rät vinkel?", "rätt": "90", "fel": ["45", "180", "75"]},
        {"fråga": "Vad är de första två decimal tecken inom PI?", "rätt": "14", "fel": ["17", "15", "12"]},
        {"fråga": "Hur räknar man ut arean av en rektangel?", "rätt": "Basen x Höjden", "fel": ["Basen x Höjden x Längden", "Höjden delad på basen", "Kvadratroten av basen"]}
    ],
    "popkultur": [
        {"fråga": "Vem spelade rollen som Harry Potter i filmerna?", "rätt": "Daniel Radcliffe", "fel": ["Snubben från 'The Green Mile'", "Tom Felton", "Elijah Wood"]},
        {"fråga": "Vilken artist skapade albumet 'IGOR'?", "rätt": "Tyler, the Creator", "fel": ["Bruno Mars", "Billie Eilish", "Fetty Wap"]},
        {"fråga": "Vem anses vara fadern av den moderna zombie genre?", "rätt": "George Romero", "fel": ["Robert Kirkman", "Danny Boyle", "Abe Forsythe"]},
        {"fråga": "Vilket år visades pilotavsnitten av 'SMILING FRIENDS' för första gången?", "rätt": "2020", "fel": ["2021", "2022", "2019"]},
        {"fråga": "Vilket år släpptes 'Graduation' av Kanye West?", "rätt": "2007", "fel": ["2006", "2000", "2012"]}
    ],
    "historia": [
        {"fråga": "Vem var Sveriges kung år 1700?", "rätt": "Karl XII", "fel": ["Gustav II Adolf", "Karl XI", "Oscar I"]},
        {"fråga": "När föll Berlinmuren?", "rätt": "1989", "fel": ["1991", "1985", "1990"]},
        {"fråga": "Vem var statsminister i Sverige under andra världskriget?", "rätt": "Per Albin Hansson", "fel": ["Tage Erlander", "Olof Palme", "Carl Gustaf Ekman"]},
        {"fråga": "I vilket land startade den industriella revolutionen?", "rätt": "Storbritannien", "fel": ["USA", "Frankrike", "Tyskland"]},
        {"fråga": "Vilket år blev Sverige medlem i EU?", "rätt": "1995", "fel": ["1990", "1993", "2001"]}
    ]
} 

alla_frågor = [] #alla_frågor är en tom lista som ska fyllas upp med resten av frågorna från frågedata dictionary
for kategori, frågor_lista in frågedata.items(): #itererar mellan varje värde och nyckel i frågedata där "kategori" är kategori, alltså 'matematik', 'vetenskap' osv.
    for data in frågor_lista: # loopar igenom varje fråga inom listan av frågor, alltså "När släpptes Graduation av Kanye west?", data innehåller även varje fråga innehåll (förutom kategori)
        fråga = Frågor(kategori, data["fråga"], data["rätt"], data["fel"]) # skapar nya frågor objekt genom att använda klassen som en slags 'konstruktor'
        alla_frågor.append(fråga) # lägger till den nya fråga objekten till listan 'alla_frågor'

# Generella funktioner / mekanik 
programledare = Person("René", 48, "Man") #Skriver in information för programledaren

"Grund funktioner"
poäng = 0 # Hur många poäng användaren har
liv = 3 # Hur många liv användaren har kvar

"Extra"
multiplier = 1 # Ökar antalet poäng om användaren når en tillräcklig lång nivå
rätt_svar= 0 # Hur många svar användaren får rätt
fel_svar = 0 # Hur många svar användaren har fått fel
counter = 0 # räknar hur många gånger while loopen har gått

"Viktig"
verifikation = 0 # Används så att användaren inte fastnar i en checkpoint loop, False betyder programmet stängs (enligt en funktion), True betyder programmet fortsätter och multiplikatorn adderas med .25

while True:
    try:
        namn = input("\nVad heter du?\n")
        ålder = int(input("\nHur gammal är du?\n"))
        kön =  input("\nVad är ditt kön?\n")

        användare = Person(namn.capitalize(), ålder, kön.capitalize()) #Tar variablerna ovanför och sparar det i variabeln användare
        
        print(f"\nSå ja {användare.get_namn()}, är du redo för frågorna?")
        input("")
        print(f"\nHörde inte vad du sa men låt oss börja med frågorna!")
        while liv != 0 and alla_frågor: #Kollar om spelaren har liv kvar och om det finns frågor kvar
            
            #CHECKPOINTS
            verifikation, multiplier = hantera_checkpoint(verifikation, multiplier, rätt_svar, poäng, fel_svar, counter)

            #FRÅGOR
            fråga = random.choice(alla_frågor) # slumpmässigt ställer en fråga
            question = fråga.ställ_fråga() # program ledaren ger användaren en fråga
            alla_frågor.remove(fråga) # tar bort frågan efter den har blivit ställt
            #Koden ovanför säkerställer att den samma fråga inte ställs igen efter den är besvarat
            counter += 1

            #SPEL
            if question == True:
                rätt_svar += 1
                poäng += 50 * multiplier # ökar poängen med ett antal av 50
                print(f"\nDu har fått {poäng} poäng!\nLåt oss fortsätta till andra frågan!")
                time.sleep(2) # väntar 2 sekunder tills nästa kod följs
                continue

            elif question == False:
                liv -= 1
                fel_svar += 1
                print(f"\nDu har {liv} chanser kvar")
                time.sleep(2)
                continue

        break

    except ValueError:
        print("\nSnälla skriv in ditt ålder med siffror, inte bokstäver!")
        continue

#SLUTET AV SPELET 
if liv == 0:
    print(f"\nEftersom du har inga mer chanser kvar så är det tyvärr sluten av spelet!")

elif liv != 0 and fel_svar == 0: # om användaren får varje svar rätt så visar detta
    time.sleep(2)
    print(f"\nVänta...")
    time.sleep(1)
    print(f"Finns inga mer frågor kvar att ställas!")
    time.sleep(1)
    print(f"\nGrattis {användare.get_namn()}! \nDu har besvarat varje fråga rätt!")
    print(f"{användare.get_namn()} du verkligen är den äkta QuizMaster!")

elif liv != 0 and fel_svar >= 1: # om användaren vinner men fick inte varje svar rätt så visar detta
    time.sleep(2)
    print(f"\nVänta...")
    time.sleep(1)
    print(f"Finns inga mer frågor kvar att ställas!")
    time.sleep(1)
    print(f"\nJag, {programledare.get_namn()} som är {programledare.get_ålder()} år gammal, gratulerar dig djupt om din vinst!")

highscore(poäng, rätt_svar, fel_svar, counter) # Highscore visas oavsett vad

