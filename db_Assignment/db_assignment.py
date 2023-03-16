

import sqlite3

conn = sqlite3.connect('db_assignment.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT \
        )")
    conn.commit()

# state file tuple
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
         'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# loop through the tuple to find .txt files
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            # x denotes values in the tuple with the file extension ".txt"
            cur.execute ("INSERT INTO tbl_files(col_filename) VALUES(?)", (x,))
            print(x)
conn.close()
