from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    rule = request.url_rule
    return render_template("index.html", rule = rule)

@app.route('/<ninja>')
def ninja(ninja):
    rule = request.url_rule
    return render_template("index.html", ninja = ninja, rule = rule)

@app.route('/ninja/<color>')
def show_ninja(color):
    rule = request.url_rule
    return render_template("index.html", color=color, rule = rule)
app.run(debug=True)
