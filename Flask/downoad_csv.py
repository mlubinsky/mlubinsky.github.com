from flask import Flask, Response
app = Flask(__name__)

@app.route("/")
def hello():
    return '''
        <html><body>
        Examples of file download in Flask
        <br>
        <a href="/getFile1">Download file by reading it and using Response().</a>
        <br>
        <a href="/getFile2">Download file <b> data/a.csv </b> by using send_file()</a>
        </body></html>
        '''

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

# Another approach: use send_file
from flask import send_file

@app.route('/getFile2') # this is a job for GET, not POST
def getFile2():
    return send_file('data/a.csv',
                     mimetype='text/csv',
                    # attachment_filename='a.csv',
                     as_attachment=True)

app.run(debug=False, port=5001)