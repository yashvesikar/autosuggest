import os
import sqlite3

import urllib.request
filepath = "./data/user-ct-test-collection-01.txt"
urllib.request.urlretrieve('http://www.cim.mcgill.ca/~dudek/206/Logs/AOL-user-ct-collection/user-ct-test-collection-01.txt', filepath)

DB_NAME = 'dashworks.db'

fp = open(filepath)
fp.readline()  # Skip the first line

CREATE_DB = not os.path.isfile(DB_NAME)
con = sqlite3.connect(DB_NAME)
cur = con.cursor()

if (CREATE_DB): 
  # Create table
  cur.execute('''CREATE TABLE collection
               (id text, query text, date text)''')

  for index, row in enumerate(fp): 
    row = row.split('\t')
    # Insert a row of data
    cur.execute(f"INSERT INTO collection VALUES (?, ?, ?)", (index, row[1], row[2]))

  # Save (commit) the changes
  con.commit()
  print("Successfully created dashworks.db")

for row in cur.execute('SELECT * FROM collection LIMIT 100'):
  print(row)
