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

class Frågor(Person):
    def __init__(self, kategori, fråga_text, rätt_svar, fel_svar):
        super().__init__(self)
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

    

def hämta_person_info(gubbe): # Hämtar allt information om användaren ifall det behövs
    return gubbe.get_namn(), gubbe.get_ålder(), gubbe.get_kön()

def hämta_fråga(fråga): #hämtar frågor och printar det lik hämta_person_info
    return fråga.get_kategori(), fråga.get_fråga_text(), fråga.get_rätt_svar(), fråga.get_fel_svar() 


while True:
    try:
        namn = input("\nVad heter du?\n")
        ålder = int(input("\nHur gammal är du?\n"))
        kön =  input("\nÄr du en man eller en kvinna?\n")

        användare = Person(namn.capitalize(), ålder, kön.capitalize()) #Tar variablerna ovanför och sparar det i variabeln användare
        programledare = Person("René", 48, "Man") #Skriver in information för programledaren
        print(hämta_person_info(användare)) #Printar allt information om användaren
        print(hämta_person_info(programledare)) #Printar allt information om programledaren

        break

    except ValueError:
        print("\nSnälla skriv in ditt ålder med siffror, inte bokstäver!")
        continue



