from flask import Flask, render_template, request, redirect, session, flash, url_for
from mysqlconnection import MySQLConnector
import re
from datetime import datetime, date
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
mysql = MySQLConnector(app,'email_validation')
app.secret_key = 'secret'
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/success', methods=['POST'])
def success():
    print "Got Post Info"
    email = request.form['email']

    if len(email) < 1:
        flash("Email cannot be empty!")
        return render_template("index.html")
    elif not EMAIL_REGEX.match(email):
        flash("Please enter a valid email")
        return render_template("index.html")
    else:
        flash("The email address you entered {} is a VALID email address! Thank you!".format(email))
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        activityQuery = "SELECT emails.email, date_format(emails.created_at, '%m/%d/%y  %r') AS created  FROM emails;"
        # We'll then create a dictionary of data from the POST data received.
        data = {
                 'email': request.form['email']
               }
        # Run query, with dictionary values injected into the query.
        mysql.query_db(query, data)
        activity = mysql.query_db(activityQuery)
        return render_template('success.html', activity = activity )
    return redirect('/success')
app.run(debug=True)
