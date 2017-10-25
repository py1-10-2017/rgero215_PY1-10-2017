from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
mysql = MySQLConnector(app,'full_friendsdb')
app.secret_key = 'secret'
friend = {}
@app.route('/')
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)
@app.route('/friends', methods=['POST'])
def create():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    error = True
    if len(first_name) < 1:
        error = True
        flash("First name cannot be empty!")
        return render_template("index.html", error= True, all_friends=friends)
    elif not first_name.isalpha() :
        error = True
        flash("First name should contain only letters")
        return render_template("index.html", error= True, all_friends=friends)
    elif len(last_name) < 1:
        error = True
        flash("Last name cannot be empty!")
        return render_template("index.html", error= True, all_friends=friends)
    elif not last_name.isalpha() :
        error = True
        flash("Last name should contain only letters")
        return render_template("index.html", error= True, all_friends=friends)
    elif len(email) < 1:
        error = True
        flash("Email cannot be empty!")
        return render_template("index.html", error= True, all_friends=friends)
    elif not EMAIL_REGEX.match(email):
        error = True
        flash("Please enter a valid email")
        return render_template("index.html", error= True, all_friends=friends)
    else:
        error = False
        flash("You successfuly added a new friend")
        # add a friend to the database!
        # Write query as a string. Notice how we have multiple values
        # we want to insert into our query.
        query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
        # We'll then create a dictionary of data from the POST data received.
        data = {
                 'first_name': first_name,
                 'last_name':  last_name,
                 'email': email
               }
        # Run query, with dictionary values injected into the query.
        mysql.query_db(query, data)
        return redirect('/')
        # return render_template("index.html", error= False, all_friends=friends)

@app.route('/friends/<id>/delete', methods=['POST'])
def delete(id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    flash("You successfuly deleted friend")
    return redirect('/')

@app.route('/friends/<id>/edit', methods=['POST'])
def edit(id):
    # Write query to select specific user by id. At every point where
    # we want to insert data, we write ":" and variable name.
    query = "SELECT * FROM friends WHERE id = :specific_id"
    # Then define a dictionary with key that matches :variable_name in query.
    data = {'specific_id': id}
    # Run query with inserted data.
    friends = mysql.query_db(query, data)
    # Friends should be a list with a single object,
    # so we pass the value at [0] to our template under alias one_friend.
    friend = friends[0]
    return render_template('edit.html', friend=friend)


@app.route('/friends/<id>', methods=['POST'])
def update(id):
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    error = True


    if len(first_name) < 1:
        error = True
        flash("First name cannot be empty!")
        return render_template("index.html", error= True, all_friends=friends)
    elif not first_name.isalpha() :
        error = True
        flash("First name should contain only letters")
        return render_template("index.html", error= True, all_friends=friends)
    elif len(last_name) < 1:
        error = True
        flash("Last name cannot be empty!")
        return render_template("index.html", error= True, all_friends=friends)
    elif not last_name.isalpha() :
        error = True
        flash("Last name should contain only letters")
        return render_template("index.html", error= True, all_friends=friends)
    elif len(email) < 1:
        error = True
        flash("Email cannot be empty!")
        return render_template("index.html", error= True, all_friends=friends)
    elif not EMAIL_REGEX.match(email):
        error = True
        flash("Please enter a valid email")
        return render_template("index.html", error= True, all_friends=friends)
    else:

        error = False
        flash("You successfuly updated a new friend")
        # add a friend to the database!
        # Write query as a string. Notice how we have multiple values
        # we want to insert into our query.
        query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :id"
        data = {
                 'first_name': first_name,
                 'last_name':  last_name,
                 'email': email,
                 'id': id
               }
        mysql.query_db(query, data)
        return redirect('/')




app.run(debug=True)
