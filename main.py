"""
projekt_2.py: druhy projekt do Engeto Online Python Akademie

author: Přemysl Harazin
email: harazinpremysl@gmail.com
"""

from random import choice



print("Hi there")
print("-------------------------------------------------------------------")
print("""I've generated a random 4 digit number for you.
Let's play a bulls and cows game.""")
print("-------------------------------------------------------------------")

def ciselny_generator(k:int)->int:
    """
    Funkce generuje k-ciferne cislo (defaultne 4-ciferne), 
    ktere nezacina 0. Vsechny cifry jsou unikatni.
    Vraci Integer.
    
    :param - int
    
    """
    ciselny_list=['1','2','3','4','5','6','7','8','9']
    helper_list=[]
    a=choice(ciselny_list)
    helper_list.append(a)
    ciselny_list.pop(ciselny_list.index(a))
    ciselny_list.insert(0,"0")
    
    for xxx in range(0,k-1):
        b=choice(ciselny_list)
        helper_list.append(b)
        ciselny_list.pop(ciselny_list.index(b))
        
    c=""
    for each in helper_list:
        c=c+each
        
    return int(c)
    
def kontrola_delky(uzivatelsky_input2 : str) -> bool:
    """
    Funkce kontrolujici uzivateluv input. 
    Input musi mit spravnou delku. 
    
    :param - str
    
    """
    
    # Kontrola Delky
    if len(uzivatelsky_input2)!=4:
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
    if uzivatelsky_input2[0]=="0":
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
    # Kontrola Duplicitni­ch Hodnot
    helper_list2=[]
    for each in uzivatelsky_input2:
        if each in helper_list2:
            print("Duplicit digits are not allowed.")
            return False
            break

        else:
            helper_list2.append(each)
    else:
        return True


vygenerovane_cislo=ciselny_generator(4) # Vygeneruje 4-ciferne cislo
# Nyni z vygenerovaneho cisla vytvari list, kazda cifra je prvek.
vygenerovane_cislo_list=[eeach for eeach in str(vygenerovane_cislo)] 

# Cyklus While, ktery bezi tak dlouho, dokud nedojde k uhodnuti spravneho cisla.
h=True
pocet_cyklu=0
while h:
    pocet_cyklu += 1
    
    # Cyklus While not, ktery kontroluje spravnost uzivatelova inputu pomoci funkci.
    zkontrolovana_hodnota1=False
    zkontrolovana_hodnota2=False
    zkontrolovana_hodnota3=False
    zkontrolovana_hodnota4=False
    while not zkontrolovana_hodnota1 or not zkontrolovana_hodnota2 or not zkontrolovana_hodnota3 or not zkontrolovana_hodnota4:
        uzivatelsky_input=input("Enter a number: ")
        zkontrolovana_hodnota1=kontrola_delky(uzivatelsky_input)
        zkontrolovana_hodnota2=kontrola_znaku(uzivatelsky_input)
        zkontrolovana_hodnota3=kontrola_nuly(uzivatelsky_input)
        zkontrolovana_hodnota4=kontrola_duplicit(uzivatelsky_input)
            
    if int(uzivatelsky_input)==vygenerovane_cislo:
        print("Correct, you've guessed the right number on the ",pocet_cyklu," try.")
        print("-------------------------------------------------------------------")
        print("That's amazing.")
        h=False
        break
    
     
    bull_count=0
    cow_count=0
    # Cyklus pocita bulls, (pokud sedi cislo i pozice)
    # a cows pokud sedi pouze cislo, ale ne pozice. 
    for z,u in zip(uzivatelsky_input,vygenerovane_cislo_list):
        if z==u:
            bull_count += 1

        if z!=u and z in vygenerovane_cislo_list:
            cow_count += 1
    
    if bull_count==1:
        print(bull_count," Bull")
    else:
        print(bull_count," Bulls")

    if cow_count==1:
        print(cow_count," Cow")
    else:
        print(cow_count," Cows")













































