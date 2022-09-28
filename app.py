import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import base64

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)
UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

class Item(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    photo = db.Column(db.LargeBinary, nullable=False)
    isActive = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return self.title


@app.route('/')
def index():
    items=Item.query.all()
    photos = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', items=items, photos=photos)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/create', methods =['POST','GET'])
def create():
    def upload_photo():
        uploaded_photo = request.files['photo']
        if uploaded_photo.filename != '':
            uploaded_photo.save(uploaded_photo.filename)

    if request.method=='POST':
        title = request.form['title']
        price = request.form['price']
        description = request.form['description']
        #photo = request.files['photo']   #.read()

        photo = request.files['photo']
        if photo(photo.filename):
            img_name = secure_filename(photo.filename)
            img_read = photo.read()
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], img_name))

        item=Item(title=title, price=price, description=description, photo=photo)

        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')

        except:
            return "Произошла ошибка"

    else:
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