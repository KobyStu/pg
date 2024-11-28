#napiste funkci, ktera podle typu "+","-","*","/" provede operaci a vrati vysledek
def operace(typ, a, b):
   vysledek = None
   if typ == "+":
        vysledek = a + b
   elif typ == "-":
        vysledek = a - b
   elif typ == "*":
        vysledek = a * b
   elif typ == "/":
        try:
            vysledek = a / b
        except ZeroDivisionError:
            print("Chyba")
            return None
   return vysledek

if __name__ == "__main__":
    operace("+",1,2) #3
    operace("-",2,1) #1
    operace("*",0,5) #0
    operace("/",4,2) #2