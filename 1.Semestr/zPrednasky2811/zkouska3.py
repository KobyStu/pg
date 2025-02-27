#
class Osoba:
    def __init__(self,jmeno,vek) -> None:
        self.jmeno = jmeno
        self.vek = vek
    

class Student(Osoba):
    def __init__(self, jmeno, vek,rocnik) -> None:
        super().__init__(jmeno, vek)
        self.rocnik = rocnik
    
    def __str__(self) -> str: #volání nadřazené metody a zavolej z ní str ->změní na přehlednější formát textu
        return f"Student {self.jmeno} studuje {self.rocnik} rocnik"
        

class Ucitel(Osoba):
    def __init__(self, jmeno, vek,obor) -> None:
        super().__init__(jmeno, vek)
        self.obor = obor

    def __str__(self) -> str:
        return f"Ucitel {self.jmeno} uci obor {self.obor}"

if __name__ == "__main__":
    student1 = Student("Adam", 20, 2)
    student2 = Student("Eva", 10, 1)
    ucitel = Ucitel("Tomas",40,"IT")

    print(student1)
    print(student2)
    print(ucitel)