from flask import Flask, render_template

app = Flask (__name__)


@app.errorhandler(404) 
def invalid_route(e): 
    return "Invalid route."

@app.route('/') #default homepage
def index():
    return "Hello World!"

@app.route('/dojo') 
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>') 
def flask(name):
    return f"Hi {name}!"

@app.route('/hello/<int:num>/<string:name>')# int is for number # string are for strings 
def hello(name,num):
    return f"Hello {name*num}"


if __name__=="__main__":
    app.run(debug=True)