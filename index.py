from flask import Flask
from flask import request
from google.cloud import bigquery

webroot = '/Users/jon/workspace/fileprocessor/'

app = Flask(__name__)

# Create a basic route
@app.route('/')
def index():
   return 'hello'

# Create a route that prints your name if specified
@app.route('/sub')
def sub():
   name = request.args.get('name')
   if name is not None:
       return 'hello ' + name
   else:
       return 'Specify a name'

# Create a route that reads in a file and outputs it to the browser
@app.route('/process')
def file():
   filename = request.args.get('filename')
   print('reading: ' + webroot + filename)

   output = ''
   with open(webroot + filename, 'r') as f:
       output = f.read().replace('\n', '<br>')
   return output

# Query a BigQuery dataset>table
@app.route('/query')
def query():
    print('input an SQL statement and sed to BigQuery')

if __name__ == "__main__":
   app.debug = True
   app.run(host='0.0.0.0')
