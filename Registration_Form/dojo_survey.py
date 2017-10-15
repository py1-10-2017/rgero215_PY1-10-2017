from flask import Flask, render_template, request, redirect, session, flash, url_for
import re
from datetime import datetime, date
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASS_REGEX = re.compile(r'\d.*[A-Z]|[A-Z].*\d')
app = Flask(__name__)
app.secret_key = 'secret'
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
@app.route('/result', methods=['POST'])
def result():
    print "Got Post Info"
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    dob = request.form['dob']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    # try:
    #     valid_date = datetime.strptime(dob, '%Y/%m/%d').date()
    #     if not (date(1940, 1, 1) <= valid_date <= date(1999, 1, 1)):
    #         flash("DOB should be in between 1940 and 1999")
    #         return render_template("index.html")
    # except:
    #     if len(email) < 1 and len(first_name) < 1 and len(last_name) < 1 and len(dob) < 1 and len(password) < 1 and len(confirm_password) < 1:
    #         flash("All fields should be filled!")
    #         return render_template("index.html")
    #     else:
    #         flash("DOB cannot be empty!")
    #         return render_template("index.html")
    if request.method == 'POST':
        if len(email) < 1 and len(first_name) < 1 and len(last_name) < 1 and len(dob) < 1 and len(password) < 1 and len(confirm_password) < 1:
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
        elif len(dob) < 1:
            flash("DOB cannot be empty!")
            return render_template("index.html")
        elif len(dob) > 1:
            try:
                valid_date = datetime.strptime(dob, '%Y/%m/%d').date()
                if not (date(1940, 1, 1) <= valid_date <= date(1999, 1, 1)):
                    flash("DOB should be in between 1940 and 1999")
                    return render_template("index.html")
            except:
                flash("DOB should be YYYY/MM/DD")
                return render_template("index.html")
            else:
                if len(password) < 1:
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
                    flash("Welcome back {}".format(first_name))
                    return render_template("result.html", first_name = first_name, last_name = last_name)
        # redirects back to the '/' route
    return redirect('/result')
app.run(debug=True) # run our server
