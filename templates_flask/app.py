from flask import render_template
from flask import Flask
import mysql.connector


app = Flask(__name__)

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="CLASH_ROYALE"
)
mycursor = mydb.cursor()


@app.route('/')
def hello():
    return render_template('hello.html', name='Daniele')


@app.route('/units')
def uniList(): 
    mycursor.execute("SELECT * FROM Clash_Unit")
    myresult = mycursor.fetchall()
    return render_template('clash_units.html', units=myresult)