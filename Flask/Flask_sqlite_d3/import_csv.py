import csv
import sqlite3

conn = sqlite3.connect('natlpark.db')
cur = conn.cursor()
cur.execute("""DROP TABLE IF EXISTS natlpark""")
cur.execute("""CREATE TABLE natlpark
            (name text, state text, year integer, area float)""")

with open('nationalparks.csv', 'r') as f:
    reader = csv.reader(f.readlines()[1:])  # exclude header line
    cur.executemany("""INSERT INTO natlpark VALUES (?,?,?,?)""",
                    (row for row in reader))
conn.commit()
conn.close()
