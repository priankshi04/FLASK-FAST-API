from flask import Flask, render_template #flask library
app = Flask(__name__) #built in variable refer to the local python file we are working with ; parameter for flask
@app.route('/')#decorator- one step before to create the function; root url
@app.route('/home')# this will result in fixing the error message that we get will include other route /home
#def hello_world():# without hardcoding
    #return '<h1>Hello World</h1>' # to make a heading
# http://127.0.0.1:5000 convention running
def home_page():
    return render_template('home.html')#handles request and direct to html files
#to refer how routing works
#set FAST_APP=market.py
#new route
