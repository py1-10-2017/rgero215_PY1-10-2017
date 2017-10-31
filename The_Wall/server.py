from flask import Flask, request, redirect, render_template, session, flash, url_for
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASS_REGEX = re.compile(r'\d.*[A-Z]|[A-Z].*\d')
app = Flask(__name__)

bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'wall')
app.secret_key = 'session'
print '*************{}'.format(app.secret_key)

@app.route('/')
def index():
    if 'login' not in session or session['login'] == False:
        return render_template('index.html')
    else:

        messages = mysql.query_db("SELECT *, DATE_FORMAT(messages.created_at, '%b %D %Y') AS created FROM messages ORDER BY id DESC;")
        for message in messages:
            created_by = message['user_id']
            user_query = "SELECT * FROM users WHERE id = :user_id"
            data = {
                'user_id' : created_by
            }
            user = mysql.query_db(user_query, data)
            message['name'] = user[0]['first_name'] +' '+ user[0]['last_name']
            message['created'] = message['created']
            message['posted_by'] = message['name'] + ' - ' + message['created']
            comment_query = "SELECT *, DATE_FORMAT(comments.created_at, '%b %D %Y') AS created FROM comments WHERE message_id = :message_id ORDER BY id DESC;"
            data = {
                'message_id' : message['id']
            }
            comments = mysql.query_db(comment_query, data)
            for comment in comments:
                created_by = comment['user_id']
                user_query = "SELECT * FROM users WHERE id = :user_id"
                data = {
                    'user_id' : created_by
                }
                comment['name'] = user[0]['first_name'] +' '+ user[0]['last_name']
                comment['created'] = comment['created']
                comment['posted_by'] = comment['name'] + ' - ' + comment['created']
            message['comments'] = comments

    return render_template("wall.html", messages_obj = messages)



@app.route('/register', methods=['POST'])
def create():
    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']


    if not EMAIL_REGEX.match(email):
        flash("Please enter a valid email")
        return render_template("index.html")
    elif not first_name.isalpha() :
        flash("First name should contain only letters")
        return render_template("index.html")
    elif not last_name.isalpha() :
        flash("Last name should contain only letters")
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
        insert_query = "INSERT INTO users (email, first_name, last_name, password, created_at, updated_at) VALUES (:email, :first_name, :last_name, :pw_hash, NOW(), NOW())"
        query_data = { 'email': email, 'first_name': first_name, 'last_name': last_name, 'pw_hash': pw_hash }
        mysql.query_db(insert_query, query_data)
        user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        user = mysql.query_db(user_query, query_data) # user will be returned in a list
        user_id = user[0]['id']
        app.secret_key = str(user_id)
        session['login'] = True
        session['user_id'] = user_id
        session['first_name'] = first_name
        session['last_name'] = last_name
        flash("Welcome {}".format(session['first_name']))
        return redirect('/')

@app.route('/login', methods=['POST'])
def login():
 email = request.form['email']
 password = request.form['password']


 if not EMAIL_REGEX.match(email):
     flash("Please enter a valid email")
     return render_template("index.html")
 elif not PASS_REGEX.match(password):
     flash("Password should have at least 1 uppercase letter and 1 numeric value")
     return render_template("index.html")
 else:
     user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
     query_data = { 'email': email }
     user = mysql.query_db(user_query, query_data) # user will be returned in a list
     try:
         if bcrypt.check_password_hash(user[0]['password'], password):
              # login user
              first_name = user[0]['first_name']
              last_name = user[0]['last_name']
              user_id = user[0]['id']
              session['login'] = True
              session['user_id'] = user_id
              app.secret_key = str(user_id)
              session['first_name'] = first_name
              session['last_name'] = last_name
              flash("Welcome {}".format(session['first_name']))
              return redirect('/')
     except:
         # set flash error message and redirect to login page
         flash("Invalid Email or Password")
         return render_template('index.html')


@app.route('/message', methods=['POST'])
def message():

    id = session['user_id']
    message = request.form['message']
    message_query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:id, :message, NOW(), NOW())"
    data = {
        'message': message,
        'id': id
    }
    mysql.query_db(message_query, data)

    return redirect('/')

@app.route('/comment', methods=['POST'])
def comment():

    id = session['user_id']
    comment = request.form['comment']
    message_id = request.form['message_id']
    comment_query = "INSERT INTO comments (message_id, user_id, comment, created_at, updated_at) VALUES (:message_id, :id, :comment, NOW(), NOW())"
    data = {
        'comment': comment,
        'id': id,
        'message_id': message_id
    }
    mysql.query_db(comment_query, data)
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True)
