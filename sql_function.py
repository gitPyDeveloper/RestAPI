from flask import Flask, redirect, url_for, request, render_template
from flask import Response , jsonify
import time
from sql_db import cl_mySQL_DB
app = Flask(__name__)


# url_for - dynamically binds URL to the defined function
@app.route('/createUser',methods = ['POST'])
def func_createUser():
    
    ticker = request.form['CreateUser']
    
    xObject = cl_mySQL_DB()
    userKey = xObject.createUser(ticker)
    #return render_template('sql_select.html')
    return 'Hello %s , save your key : %s' %(ticker , userKey)



@app.route('/data',methods = ['GET'])
def func_fetchData():

    ticker = request.args.get('ticker')
    field = request.args.get('field')
    source = request.args.get('source')
    in_key = request.args.get('key')
    print in_key
    

    if in_key is None:
        in_key = "0"

    xObject = cl_mySQL_DB()
    dict_table = xObject.getTicker(ticker, field, source, in_key)
    xObject.closeConnection()
    
    #return render_template('sql_display.html',result = dict_table)
    return '%s'  %dict_table
