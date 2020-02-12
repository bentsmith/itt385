import flask
from flask import Flask

DEBUG = 1

app = flask.Flask(__name__)  # set up the Flask Framework

if DEBUG > 0:
    app.debug = True


@app.route("/test")
def show_test():
    return flask.render_template("test.html")

@app.route("/test2")
def show_test2():
    return flask.render_template("test2.html", fromname="From Me")

@app.route("/test3/<toname>")
def show_test3(toname):

    fromname="ben"
    return flask.render_template("test3.html", fromname=fromname, toname=toname)
app.run()
