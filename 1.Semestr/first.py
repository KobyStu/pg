#def hello_world():
  #  print("Hello World!")

#vypíše 'limit' hvězdiček, po každém cyklu přičte 1, dokud nebude stejné jako 'limit' 
def five_stars(limit): 
    i = 0
    while i < limit: 
        print('*')
        i += 1
#five_stars(2)

#Ověří, zda je číslo v rozezí minimum - maximum a vypíše textový výstup
def je_v_rozsahu(number,minimum,maximum):
    pass #nic nedělá, ale nerozbíjí syntaxi před tím než je funkc naplněna
    if number >= minimum and number <= maximum:
        print("Číslo ",number," je v rozsahu", minimum , " a ", maximum)
    else :
        print("Číslo ", number," je mimo rozsah", minimum , " a ", maximum)

#je_v_rozsahu(10,100,1000)
#"Out of Range"
#je_v_rozsahu(500,100,1000)
#"In range"

#ze tří čísel vybere to největší
def max_number(a, b, c):
    if a > b and a > c :
        print(a)
    elif b > a and b >= c:
        print(b)
    elif c > a and c >= b:
        print(c)

#max_number(1,2,3)
#3
#max_number(100,10,1)
#100
#max_number(1.1,1.2,1.3)
#1.3

#Vypracování úkolu 1
def sudy_nebo_lichy(cislo):
   if cislo % 2 > 0: #Pokud zbytek po dělení je větší než 0, platí else
      print("Číslo X je liché")
   else:
       print("Číslo X je sudé")

sudy_nebo_lichy(5)
sudy_nebo_lichy(1000000)