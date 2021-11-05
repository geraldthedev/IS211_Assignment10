import sqlite3 as sqli

con = None

person =(
    (1,'James','Smith',41),
    (2,'Diana','Greene',23),
    (3,'Sara','White',27),
    (4,'William','Gibson',23)
)

pet =(
    (1,'Rusty','Dalmation',4,1),
    (2,'Bella','Alaskan Malamute',3,0),
    (3,'Max','Cocker Spaniel',1,0),
    (4,'Rocky','Beagle',7,0),
    (5,'Rufus','Cocker Spaniel',1,0),
    (6,'Spot','Bloodhound',2,1)

)

person_pet =(
    (1,1),
    (1,2),
    (2,3),
    (2,4),
    (3,5),
    (4,6)

)

con = sqli.connect('pets.db')
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS person( id INTEGER PRIMARY KEY,first_name TEXT,last_name TEXT,age INTEGER)")

cur.execute("CREATE TABLE IF NOT EXISTS pet(id INTEGER PRIMARY KEY,name TEXT,breed TEXT,age INTEGER,dead INTEGER)")

cur.execute("CREATE TABLE IF NOT EXISTS person_pet(person_id INTEGER, pet_id INTEGER)")

cur.executemany("INSERT INTO person VALUES(?, ?, ?, ?)", person)
cur.executemany("INSERT INTO pet VALUES(?, ?, ?, ?, ?)", pet)
cur.executemany("INSERT INTO person_pet VALUES(?, ?)", person_pet)

con.commit()


person_data = cur.execute('SELECT * FROM person').fetchall()

pet_data = cur.execute('SELECT * FROM pet').fetchall()

pet_id = cur.execute('SELECT * FROM person_pet').fetchall()

print(person_data)
print(pet_data)
print(pet_id)

con.close()
if __name__ == "__main__":
    pass
