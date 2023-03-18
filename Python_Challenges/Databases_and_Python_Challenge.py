

import sqlite3
from sqlite3 import *

rosterValues = (('Jean-Baptiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100), ('Ak\'not', 'Mangalore', -5))

def create_connection():
    conn = sqlite3.connect(':memory:')
    c = connect.cursor()
    c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT")
    c.execute("INSERT INTO Roster VALUES (?, ?, ?)", rosterValues)
        
    c.execute("UPDATE Roster SET Species = ? WHERE Name = ?", ('Human', 'Korben Dallas'))

    c.execute("SELECT Name, IQ FROM Roster WHERE Species = Human")
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)
