from flask import Flask, request, g, abort, jsonify
import sqlite3, hashlib, os
import json
# marshallow

app = Flask(__name__)
DATABASE="database.db"

def connect_to_database():
    return sqlite3.connect(DATABASE)
    #return sqlite3.connect(app.config['DATABASE'])

def get_db():
    db = getattr(g, 'db', None)
    if db is None:
        db = g.db = connect_to_database()
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

def readSQL(query, args=()):
    cur = get_db().execute(query, args)
    rows = cur.fetchall()
    cur.close()
    return rows

def writeSQL(query, args=()):
     get_db().execute(query, args)
     get_db().commit()

#Example: pathroute
#    hostname:i5000/pathroute/p1/p2/p3
#    @app.route("/pathroute/<path:mypath>" )
#    def pathroute(mypath):
#              print mypath    - returns p1/p2/p3
#
#


@app.route("/api/v1/user", methods = ['GET'])
def get_all_users():
   SQL = "SELECT firstName FROM users"
   print (SQL)
   rows = readSQL(SQL)
   print (rows)
   return jsonify({"users": rows})

@app.route("/api/v1/user/<string:firstName>", methods = ['GET'])
def get_user(firstName):
   print ("GET Individual user", firstName)
   SQL = "SELECT * FROM users where firstName=?"
   print (SQL)
   rows = readSQL(SQL, (firstName,))
   print (rows)
   return jsonify({"users": rows})

@app.route("/api/v1/user/<string:firstName>", methods = ['DELETE'])
def delete_user(firstName):
   SQL = "DELETE FROM users where firstName=?"
   print (SQL)
   writeSQL(SQL, (firstName,))

   return jsonify({"users": firstName })

@app.route("/api/v1/user", methods = ['POST'])
def create_user():
    print("-- post --")
    if not request.json:
          err = "Error - no request.json"
          print (err)
          return jsonify({'ERROR':1}), 401

    print(request.json)
    if not 'firstName' in  request.json:
       print ("No firstName in request.json")
    else:
        firstName=request.json['firstName']

    print (firstName)
    SQL="INSERT INTO  users (firstName) VALUES (?)"
    writeSQL(SQL, (firstName,))
    print ("SUCCESS")
    #return json.dumps(request.json), 201   # shell return the id as well
    return jsonify(request.json), 201   # shell return the id as well

if __name__ == '__main__':
    app.run(debug=True, port=5009)
