import json #Stáhnout z Githubu !!!

class BadDataError(Exception):
    pass

class Souradnice:

    def _init_(self,sirka, delka):
        self.sirka = sirka
        self.delka = delka

    def _str_(self) -> str:
        return f'Souradnice: {self.sirka}, {self.delka}'
    
    @classmethod
    def nacti_z_dat(cls, data):
        if "souradnice" not in data:
            raise BadDataError
        

if __name__ == "__main__":

    data = {"souradnice": {"sirka": 50, "delka": 50}}

    s = Souradnice.nacti_z_dat(data)

    print(s)