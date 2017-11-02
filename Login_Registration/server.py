from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASS_REGEX = re.compile(r'\d.*[A-Z]|[A-Z].*\d')
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'login_registration')
app.secret_key = 'session'
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/register', methods=['POST'])
def create():
    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    if len(email) < 1 and len(first_name) < 1 and len(last_name) < 1 and len(password) < 1 and len(confirm_password) < 1:
        flash("All fields should be filled!")
        return render_template("index.html")
    elif len(email) < 1:
        flash("Email cannot be empty!")
        return render_template("index.html")
    elif not EMAIL_REGEX.match(email):
        flash("Please enter a valid email")
        return render_template("index.html")
    elif len(first_name) < 1:
        flash("First name cannot be empty!")
        return render_template("index.html")
    elif not first_name.isalpha() :
        flash("First name should contain only letters")
        return render_template("index.html")
    elif len(last_name) < 1:
        flash("Last name cannot be empty!")
        return render_template("index.html")
    elif not last_name.isalpha() :
        flash("Last name should contain only letters")
        return render_template("index.html")
    elif len(password) < 1:
        flash("Password cannot be empty!")
        return render_template("index.html")
    elif len(confirm_password) < 1:
        flash("Password Confirmation cannot be empty!")
        return render_template("index.html")
    elif len(password) > 1 and len(password) < 8:
        flash("Password should be more than 8 characters!")
        return render_template("index.html")
    elif not PASS_REGEX.match(password):
        flash("Password should have at least 1 uppercase letter and 1 numeric value")
        return render_template("index.html")
    elif confirm_password != password:
        flash("Password and Password Confirmation should match")
        return render_template("index.html")
    else:
        pw_hash = bcrypt.generate_password_hash(password)
        flash("Welcome {}".format(first_name))
        insert_query = "INSERT INTO users (email, first_name, last_name, pw_hash, created_at, updated_at) VALUES (:email, :first_name, :last_name, :pw_hash, NOW(), NOW())"
        query_data = { 'email': email, 'first_name': first_name, 'last_name': last_name, 'pw_hash': pw_hash }
        mysql.query_db(insert_query, query_data)
        user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        user = mysql.query_db(user_query, query_data) # user will be returned in a list
        app.secret_key = user[0]['id']
        return render_template("access.html", first_name = first_name, last_name = last_name)

@app.route('/login', methods=['POST'])
def login():
 email = request.form['email']
 password = request.form['password']
 user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
 if len(email) < 1 and len(password) < 1:
     flash("All fields should be filled!")
     return render_template("index.html")
 elif len(email) < 1:
     flash("Email cannot be empty!")
     return render_template("index.html")
 elif not EMAIL_REGEX.match(email):
     flash("Please enter a valid email")
     return render_template("index.html")
 elif len(password) < 1:
     flash("Password cannot be empty!")
     return render_template("index.html")
 elif not PASS_REGEX.match(password):
     flash("Password should have at least 1 uppercase letter and 1 numeric value")
     return render_template("index.html")
 else:
     try:
         query_data = { 'email': email }
         user = mysql.query_db(user_query, query_data) # user will be returned in a list
         if bcrypt.check_password_hash(user[0]['pw_hash'], password):
          # login user
          first_name = user[0]['first_name']
          last_name = user[0]['last_name']
          app.secret_key = user[0]['id']
          flash("Welcome {}".format(first_name))
          return render_template("access.html", first_name = first_name, last_name = last_name)
     except:
         # set flash error message and redirect to login page
         flash("Invalid Email or Password")
         return redirect('/')


app.run(debug=True)
