import random

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
            else:
                print(f"Fel! Rätt svar var: {self.__rätt_svar}")
        
        except:
            print("Ogiltig svar.")
            

#FUNKTIONER
def hämta_person_info(gubbe): # Hämtar allt information om användaren ifall det behövs
    return gubbe.get_namn(), gubbe.get_ålder(), gubbe.get_kön()

def hämta_fråga(fråga): #hämtar frågor och printar det lik hämta_person_info() funktionen ovanför
    return fråga.get_kategori(), fråga.get_fråga_text(), fråga.get_rätt_svar(), fråga.get_fel_svar() 

#FRÅGOR

"vetenskap"
q1 = Frågor("Vetenskap", "Vad heter den största planet i vårt solsystem?", "Jupiter", ["Saturnus", "Mars", "Jorden"]) #Sista kategorin ligger i en lista så att mer än 1 fråga kan passa i fel fråga kategorin
q2 = Frågor("Vetenskap", "Vilket grundämne har kemiska beteckningen O?", "Syre", ["Väte", "Kväve", "Kol"])
q3 = Frågor("Vetenskap", "Hur många ben har en vuxen människa normalt?", "206", ["207", "201", "212"])
q4 = Frågor("Vetenskap", "Vad kallas den process där växter omvandlar solljus till energi?", "Fotosyntes", ["Förbränning", "Cellandning", "Fermentering"])
q5 = Frågor("Vetenskap", "Vilken vetenskapsmän formulerade gravitationslagen?", "Isaac Newton", ["Albert Einstein", "Galileo Galilei", "Nikola Tesla"])

"matte"
q6 = Frågor("Matematik", "Vad är 7 x 8?", "56", ["54", "67", "49"])
q7 = Frågor("Matematik", "Vad är roten ur 144?", "12", ["14", "11", "8"])
q8 = Frågor("Matematik", "Hur många grader är en rät vinkel?", "90", ["45", "180", "75"])
q9 = Frågor("Matematik", "Vad är de första två decimal tecken inom PI?", "14", ["17", "15", "12" ])
q10 = Frågor("Matematik", "Hur räknar man ut arean av en rektangel?", "Basen x Höjden", ["Basen x Höjden x Längden", "Höjden delad på basen", "Kvadratroten av basen"])

"popkultur"
q11 = Frågor("Popkultur", "Vem spelade rollen som Harry Potter i filmerna?", "Daniel Radcliffe", ["Snubben från 'The Green Mile'", "Tom Felton", "Elijah Wood"])
q12 = Frågor("Popkultur", "Vilken artist skapade albumet 'IGOR'?", "Tyler, the Creator", ["Bruno Mars", "Billie Eilish", "Fetty Wap"] )
q13 = Frågor("Popkultur", "Vem anses vara skaparen av moderna film zombies?", "George Romero", ["Robert Kirkman", "Danny Boyle", "Abe Forsythe"])
q14 = Frågor("Popkultur", "Vilket år visades pilotavsnitten av 'smiling friends' för första gången?", "2020", ["2021", "2022", "2019"])
q15 = Frågor("Popkultur", "Vilket år släpptes 'Graduation' av Kanye West?", "2007", ["2006", "2000", "2012"])

"historia"
q16 = Frågor("Historia", "Vem var Sveriges kung år 1700?", "Karl XII", ["Gustav II Adolf", "Karl XI", "Oscar I"])
q17 = Frågor("Historia", "När föll Berlinmuren?", "1989", ["1991", "1985", "1990"])
q18 = Frågor("Historia", "Vem var statsminister i Sverige under andra världskriget?", "Per Albin Hansson", ["Tage Erlander", "Olof Palme", "Carl Gustaf Ekman"])
q19 = Frågor("Historia", "I vilket land startade den industriella revolutionen?", "Storbritannien", ["USA", "Frankrike", "Tyskland"])
q20 = Frågor("Historia", "Vilket år blev Sverige medlem i EU?", "1995", ["1990", "1993", "2001"])

#FRÅGOR SAMLING
vetenskap_frågor = [q1, q2, q3, q4, q5]
matematik_frågor = [q6, q7, q8, q9, q10]
popkultur_frågor = [q11, q12, q13, q14, q15]
historia_frågor = [q16, q17, q18, q19, q20]

alla_frågor =[q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20]

while True:
    try:
        namn = input("\nVad heter du?\n")
        ålder = int(input("\nHur gammal är du?\n"))
        kön =  input("\nÄr du en man eller en kvinna?\n")

        användare = Person(namn.capitalize(), ålder, kön.capitalize()) #Tar variablerna ovanför och sparar det i variabeln användare
        programledare = Person("René", 48, "Man") #Skriver in information för programledaren
        print(hämta_person_info(användare)) #Printar allt information om användaren
        print(hämta_person_info(programledare)) #Printar allt information om programledaren

        print(f"Så ja {användare.get_namn()}, är du redo för frågorna?")
        input("")
        print(f"Sorgligen nog kan jag inte förstå det, fast så börjar vi med frågorna!")
        random.choice(alla_frågor).ställ_fråga()

        break

    except ValueError:
        print("\nSnälla skriv in ditt ålder med siffror, inte bokstäver!")
        continue



