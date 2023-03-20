

import sqlite3
from sqlite3 import *

#   One of the requirements for the challenge is to make the db in RAM
conn = sqlite3.connect(':memory:')

rosterValues = (('Jean-Baptiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100), ('Ak\'not', 'Mangalore', -5))

def create_connection():
    c = conn.cursor()
    c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")
    conn.commit()
    
    c.executemany("INSERT INTO Roster VALUES (?, ?, ?)", rosterValues)
    conn.commit()
        
    c.execute("UPDATE Roster SET Species = ? WHERE Name = ?", ('Human', 'Korben Dallas'))
    conn.commit()

    c.execute("DELETE FROM Roster WHERE Name = ?", ('Ak\'not',))
    conn.commit()

    c.execute("SELECT Name, IQ FROM Roster")
    rows = c.fetchall()
    for row in rows:
        print(row)

create_connection()
