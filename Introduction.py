from flask import Flask #flask library
app = Flask(__name__) #built in variable refer to the local python file we are working with ; parameter for flask
@app.route('/') #decorator- one step before to create the function; root url
def hello_world():
    return '<h1>Hello World</h1>' # to make a heading

# http://127.0.0.1:5000 convention running
#set FLASK_DEBUG=1 cmd to change the debug mode, to connect the the url changes and not to restart the web browser again
#need to set off while deploying it , so the client cant change
@app.route('/about/<username>') #which url i want to enable ; as much routes we can build
def about_page(username):#parameter
    return f'<h1>This is the about page of {username}</h1>'
#add the url if we add /about it would get the about_page fn and return the given output
#USING DYNAMIC ROUTES- can be used when multiple people want to see profile info like facebook
#can write any name http://127.0.0.1:5000/about/Jim in the url to get that return in the web page 