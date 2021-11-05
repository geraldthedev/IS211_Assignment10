import sqlite3 as sqli


def findPets():
    
    con = sqli.connect('pets.db')
    cur = con.cursor()
    ask = input("what is the id? ")
    
    owner= cur.execute('SELECT * FROM person where id =?', (ask,)).fetchone()
    pet= cur.execute('SELECT * FROM pet WHERE id=?',(ask,)).fetchone()
    
    profile={"owner_list":[str(owners) for owners in owner],"pet_list":[str(pets) for pets in pet]}

    pet_owner= {
        "ID": profile["owner_list"][0],
        "First Name":profile["owner_list"][1],
        "Last Name":profile["owner_list"][2],
        "Age":profile["owner_list"][3],
        "Pet Name":profile["pet_list"][1],
        "Pet Breed":profile["pet_list"][2],
        "Pet Age":profile["pet_list"][3],
        "Deceased":profile["pet_list"][4]
    }
    
    for owners in pet_owner:
        print(str(owners) + ": " + str(pet_owner[owners]))
   



findPets()

if __name__ == "__main__":
    pass
