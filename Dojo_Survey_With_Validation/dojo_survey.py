from flask import Flask, render_template, request, redirect, session, flash
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
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    if request.method == 'POST':
       if len(name) < 1:
           flash("Name cannot be empty!")
           return render_template("index.html")
       elif len(comment) < 1:
            flash("Comment cannot be empty!")
            return render_template("index.html")
       elif len(comment) > 120:
            flash("Comment cannot be longer than 120 characters!")
            return render_template("index.html")
       else:
           flash("Thank you {}, your message was successfully submitted".format(name))
           return render_template("result.html", name = name, location = location, language = language, comment = comment)
       # redirects back to the '/' route
    return redirect('/result')
app.run(debug=True) # run our server
