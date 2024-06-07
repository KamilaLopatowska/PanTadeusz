from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template("index.html.jinja")

@app.route('/contents')
def contents():
    return render_template("contents.html.jinja")

@app.route('/k1.html')
def k1():
    return render_template("k1.html.jinja")

@app.route('/k2.html')
def k2():
    return render_template("k2.html.jinja")

@app.route('/k3.html')
def k3():
    return render_template("k3.html.jinja")

@app.route('/k4.html')
def k4():
    return render_template("k4.html.jinja")

@app.route('/k5.html')
def k5():
    return render_template("k5.html.jinja")

@app.route('/k6.html')
def k6():
    return render_template("k6.html.jinja")

@app.route('/k7.html')
def k7():
    return render_template("k7.html.jinja")

@app.route('/k8.html')
def k8():
    return render_template("k8.html.jinja")

@app.route('/k9.html')
def k9():
    return render_template("k9.html.jinja")

@app.route('/k10.html')
def k10():
    return render_template("k10.html.jinja")

@app.route('/k11.html')
def k11():
    return render_template("k11.html.jinja")

@app.route('/k12.html')
def k12():
    return render_template("k12.html.jinja")