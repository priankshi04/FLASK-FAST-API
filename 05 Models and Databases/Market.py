from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///market.db'

db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(),primary_key =True)
    name = db.Column(db.String(length =50),nullable = False , unique = True)
    price = db.Column(db.Integer(),nullable= False )
    barcode= db.Column(db.String(length =12),nullable= False , unique = True)
    description = db.Column(db.String(length =1024),nullable = False,unique = True)
    def __repr__(self):
        return f"Item(id={self.id}, name='{self.name}', price={self.price}, barcode='{self.barcode}', description='{self.description}')"


@app.route('/')
@app.route('/home')
def home():
    return render_template('/home.html')
@app.route('/market')
def market():
    item = Item.query.all()
    print(item)
    return render_template('/market.html',items=item)

if __name__=="__main__":
    app.run(debug="True")
