#http://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask
#http://www.programcreek.com/python/example/58917/flask.send_file

from flask import Flask, Response
app = Flask(__name__)
################################################
@app.route("/")
def hello():
    return '''
        <html><body>
        Examples of file download in Flask
        <br>
        <a href="/getFile1">Download file by reading it and using Response()</a>
        <br>
        <a href="/getFile2">Download file <b> data/a.csv </b> using send_file()</a>
        <br>
        <a href="/static/b.txt">Download file <b>b.txt</b> from /static folder <b>ONLY</b> using send_static_file()</a>
        <br>
        <a href="/zip">ZIP and Download a.111 into capsule.zip  using send_file()</a>

        </body></html>
        '''
#################################################
@app.route("/getFile1")
def getFile1():
    # with open("outputs/Adjacency.csv") as fp:
    #     csv = fp.read()
    csv = '1,2,3\n4,5,6\n' # this is the cheating to eliminating the reading the file

    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=myplot.csv"})
###############################################
# Another approach: use send_file
from flask import send_file

@app.route('/getFile2') # this is a job for GET, not POST
def getFile2():
    return send_file('data/a.csv',
                     mimetype='text/csv',
                    # attachment_filename='a.csv',
                     as_attachment=True)

###############################################
from io import BytesIO
import gzip
import zipfile
import time
import os

@app.route('/zip') # this is a job for GET, not POST
def getZip():

# write bytes to zip file in memory
#myio = BytesIO()
#g = gzip.GzipFile(fileobj=myio, mode='wb')
#g.write(b"does it work")
#g.close()
#myio.seek(0)
# read bytes from zip file in memory
#g = gzip.GzipFile(fileobj=myio, mode='rb')
#result = g.read()
#g.close()
#print(result)
  fileName="a.111"
  memory_file = BytesIO()
  with zipfile.ZipFile(memory_file, 'w') as zf:
        zf.write(fileName, os.path.basename(fileName), zipfile.ZIP_DEFLATED)
  
  memory_file.seek(0)
  return send_file(memory_file, attachment_filename='capsule.zip', as_attachment=True)
####################################################################################
@app.route('/static/<path:path>')
def static_file(path):
    return app.send_static_file(path)

##############################################
app.run(debug=False, port=5001)