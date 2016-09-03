#import mysql
#dir(mysql)
import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='abe')

cursor = cnx.cursor()

query = ("SELECT id, v FROM t "
         "WHERE id BETWEEN %s AND %s")

id_start = -1  
id_end   = 10   

cursor.execute(query, (id_start, id_end))

for (id, v) in cursor:
  print("{}, {} ".format( id, v))

cursor.close()
cnx.close()
