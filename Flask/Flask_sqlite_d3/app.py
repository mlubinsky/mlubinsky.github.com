#import csv
import logging
import sqlite3
import time

from flask import Flask, request, g
from flask import render_template

#DATABASE = 'natlpark.db'
DATABASE = 'bart.db'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_to_database():
    return sqlite3.connect(app.config['DATABASE'])

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

def execute_query(query, args=()):
    print "SQL=", query
    cur = get_db().execute(query, args)
    rows = cur.fetchall()
    cur.close()
    return rows

@app.route("/")
def root():
     return """ 
         <p> <a href="http://127.0.0.1:5000/viewdb">viewdb</a>
         <p> <a href="http://127.0.0.1:5000/plot">plot</a>
         <p> <a href="http://127.0.0.1:5000/dest/Fremont">dest/Fremont</a>
         <p> <a href="http://127.0.0.1:5000/static/graph.html">d3</a> 
     """


@app.route('/plot')
def show_entries():
    #db = get_db()
    #cur = db.execute('select dest, etd from etd')
    #entries = cur.fetchall()
    rows = execute_query("""SELECT * FROM etd""")
    return render_template('plot.html', entries=rows)


# You can point your browser at (my public DNS)/?dest=Fremont&time=12:17&station=plza&day=0 to get csv formatted data ready to pass into D3.js for graphing.
@app.route("/data")
def print_data():
    """Respond to a query of the format:
    myapp/?dest=Fremont&time=600&station=plza&day=0
    with ETD data for the time and location specified in the query"""
    start_time = time.time()
    cur = get_db().cursor()
    try:
        minute_of_day = int(request.args.get('time'))
    except ValueError:
        return "Time must be an integer"
    station = request.args.get('station')
    print minute_of_day
    day = request.args.get('day')
    dest = request.args.get('dest')
    result = execute_query(
        """SELECT etd, count(*)
           FROM etd
           WHERE dest = ? AND minute_of_day = ?
                 AND station = ? AND day_of_week = ?
           GROUP BY etd""",
        (dest, minute_of_day, station, day)
    )
    str_rows = [','.join(map(str, row)) for row in result]
    query_time = time.time() - start_time
    logging.info("executed query in %s" % query_time)
    cur.close()
    header = 'etd,count\n'
    return header + '\n'.join(str_rows)


@app.route("/viewdb")
def viewdb():
    rows = execute_query("""SELECT * FROM etd""")
    return '<br>'.join(str(row) for row in rows)

@app.route("/dest/<city>")
def sortby(city):
    print "city.title()=",
    print city.title()
    
    rows = execute_query("""SELECT * FROM etd WHERE dest = ?""",
                         [city.title()])
    return '<br>'.join(str(row) for row in rows)

if __name__ == '__main__':
  app.run(debug=True)
