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
    def __init__(self, namn, fråga):
        super().__init__(self, namn)
        self.__fråga = fråga
    
    def get_fråga(self):
        return self.__fråga
    
    def set_fråga(self, fråga):
        self.__fråga = fråga

def frågor(x, y):
    y = ["Sport", "Historia", "Vetenskap", "Popkultur", "Sånger"]
    


#while True:
 #   try:
  #      namn = input("\nVad heter du?\n")
   #     ålder = int(input("\nHur gammal är du?\n"))
    #    kön =  input("\nÄr du en man eller en kvinna?\n")

     #   användare = Person(namn.capitalize(), ålder, kön.capitalize())
      #  programledare = Frågor(programledare.set_namn("René"), programledare.get_namn(), programledare)

       # print(användare.get_namn(), användare.get_ålder(), användare.get_kön())
        #break

    #except ValueError:
     #   print("\nSnälla skriv in ditt ålder med siffror, inte bokstäver!")
      #  continue

