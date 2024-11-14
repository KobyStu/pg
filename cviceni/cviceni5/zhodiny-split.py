#Zkopirovat si soubory později z učitelova repozitáře!!!!!!!!!
import sys

def read_data(file_name):
    data = []
    with open(file_name,"r") as file:
        for line in file:
           print(line.split)
    # 1000

def write_data(file_name,data):
   with open(file_name,"w") as file:
      
    if __name__ == "__main__":
        try:
            file = sys.argv[1]
            data = read_data(file)
            print(data)
            text = "Alice,Bob,Tomas"
            split_text = text.split(',')
            print(split_text)
        except FileNotFoundError:
            print("Chyba: Soubor nebyl nalezen/neexistuje.")
        except IndexError:
            print("Chyba: Nebyly zadány soubory")
    

    #otevrit soubor, cist po řadčich, rozseknout pomoci splitu a dat dohromady
    