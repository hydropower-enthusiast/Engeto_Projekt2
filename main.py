"""
projekt_2.py: druhy projekt do Engeto Online Python Akademie

author: Přemysl Harazin
email: harazinpremysl@gmail.com
"""

from random import sample


print("Hi there")
print("-------------------------------------------------------------------")
print("""I've generated a random 4 digit number for you.
Let's play a bulls and cows game.""")
print("-------------------------------------------------------------------")

def ciselny_generator(k:int)->str:
    """
    Funkce generuje k-ciferne cislo (defaultne 4-ciferne), 
    ktere nezacina 0. Vsechny cifry jsou unikatni.
    Vraci String.
    
    Ciste teoreticky... tento styl generovani muze bezet temer do nekonecna, 
    jelikoz generovane cislo muze neustale zacinat nulou, ale prakticky
    to tak neni, jelikoz sance na generovani dalsich cisel zacinajicich 
    opet nulou se snizuje.
    
    :param - int
    
    """
    pomocny_list=[0]*k
    while pomocny_list[0] == 0:
        pomocny_list = sample(range(0,10),k)
    
    vygenerovane_cislo = ''.join(map(str, pomocny_list))
    print(vygenerovane_cislo)
    return vygenerovane_cislo

def kontrola_inputu(uzivatelsky_input2 : str) -> bool:
    """
    Funkce zastresujici celkovou kontrolu inputu.
    Obsahuje dalsi kontrolni funkce. 
        
    :param - str
        
    """
    
    def kontrola_delky(uzivatelsky_input2 : str) -> bool:
        """
        Funkce kontrolujici uzivateluv input. 
        Input musi mit spravnou delku. 
        
        :param - str
        
        """
        
        # Kontrola Delky
        if len(uzivatelsky_input2) != 4:
            print("Given number does not have the proper length")
            return False
        else:
            return True
        
    def kontrola_znaku(uzivatelsky_input2 : str) -> bool:
        """
        Funkce kontrolujici uzivateluv input. 
        Input musi byt cisla.
    
        
        :param - str
        
        """    
            
        try:
            int(uzivatelsky_input2)
            return True
        except ValueError:
            print("Some signs are not numbers")
            return False
    
    
    def kontrola_nuly(uzivatelsky_input2 : str) -> bool:
        """
        Funkce kontrolujici uzivateluv input. 
        Input nesmi zacinat 0.
        
        :param - str
        
        """ 
            
        # Kontrola, zda ci­slo nezacina 0
        if uzivatelsky_input2[0] == "0":
            print("Number cannot start with 0")
            return False
        else:
            return True
    
    def kontrola_duplicit(uzivatelsky_input2 : str) -> bool:
        """
        Funkce kontrolujici uzivateluv input. 
        Cifry se nesmi opakovat.
        
        :param - str
        
        """     
        # Kontrola Duplicitni­ch Hodnot#
        helper_list2=[]
        for each in uzivatelsky_input2:
            if each in helper_list2:
                print("Duplicit digits are not allowed.")
                return False
            else:
                helper_list2.append(each)
        else:
            return True

    # Nasleduje volani jednotlivych kontrol
    a = kontrola_delky(uzivatelsky_input2)
    b = kontrola_znaku(uzivatelsky_input2)
    try:
        c = kontrola_nuly(uzivatelsky_input2)
    except IndexError:
        c = False
    d = kontrola_duplicit(uzivatelsky_input2)
    
    # Vyhodnoceni kontrol a navrat True/False
    if not a or not b or not c or not d:
        return False
    else:
        return True


def main():
    vygenerovane_cislo = ciselny_generator(4)
    # Vygeneruje 4-ciferne cislo
    
    # Cyklus While, ktery bezi tak dlouho, dokud nedojde k 
    # uhodnuti spravneho cisla.
    h = True
    pocet_cyklu = 0
    while h:
        pocet_cyklu += 1
        
        # Cyklus While not, ktery kontroluje spravnost uzivatelova 
        # inputu pomoci funkci.
        zkontrolovana_hodnota = False
        while not zkontrolovana_hodnota:
            uzivatelsky_input = input("Enter a number: ")
            zkontrolovana_hodnota = kontrola_inputu(uzivatelsky_input)

        # Pokud dojde k uhodnuti, dojde k zastaveni cyklu while. 
        # break je pouzit zamerne, aby po uhodnuti spravneho cisla
        # nedoslo k vypisu poctu 4 bulls a 0 cows.
        if uzivatelsky_input == vygenerovane_cislo:
            print("Correct, you've guessed the right number on the ", pocet_cyklu, " try.")
            print("-------------------------------------------------------------------")
            print("That's amazing.")
            h = False
            break
        
         
        bull_count = 0
        cow_count = 0
        # Cyklus nejprve propoji odpovidajici cifry pomoci zipu 
        # inputu a generov. cisla a nasledne 
        # pocita bulls, (pokud sedi cislo i pozice)
        # a cows pokud sedi pouze cislo, ale ne pozice. 
    
        for cifra_input,cifra_generator in zip(uzivatelsky_input,vygenerovane_cislo):
            if cifra_input == cifra_generator:
                bull_count += 1
    
            if cifra_input != cifra_generator and cifra_input in vygenerovane_cislo:
                cow_count += 1
        
        if bull_count == 1:
            print(bull_count, " Bull")
        else:
            print(bull_count, " Bulls")
    
        if cow_count == 1:
            print(cow_count, " Cow")
        else:
            print(cow_count, " Cows")

# Schovani funkce main do teto podminky umoznuje vyhnout se automatickemu 
# spousteni skriptu pri importu. 
if __name__ == "__main__":
    main()






































