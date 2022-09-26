from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///shop.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    photo = db.Column(db.LargeBinary, nullable=False)
    isActive = db.Column(db.Boolean, default=True)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/shuby')
def shuby():
    return render_template('shuby.html')

@app.route('/dublenki')
def dublenki():
    return render_template('dublenki.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/dostavka')
def dostavka():
    return render_template('dostavka.html')

@app.route('/basket')
def basket():
    return render_template('basket.html')

@app.route('/opt')
def opt():
    return render_template('opt.html')



if __name__=='__main__':
    app.run(debug=True)