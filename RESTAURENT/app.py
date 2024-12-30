import os
from flask import Flask, flash, redirect, render_template, request, session, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant.db'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Define the Reservation model
class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    date = db.Column(db.String(10), nullable=False)
    time = db.Column(db.String(5), nullable=False)
    guests = db.Column(db.Integer, nullable=False)
    requests = db.Column(db.Text, nullable=True)

# Define the Contact model 
class Contact(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(100), nullable=False) 
    email = db.Column(db.String(120), nullable=False) 
    message = db.Column(db.Text, nullable=False)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register user"""
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirmation = request.form.get('confirmation')

        if not username:
            return "must provide username", 400
        elif not email:
            return "must provide email", 400
        elif not password:
            return "must provide password", 400
        elif password != confirmation:
            return "passwords don't match", 400

        hash_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, email=email, password=hash_password)

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        except:
            return "username or email already exists", 400

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Log user in"""
    session.clear()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username:
            flash("Must provide username", "danger")
            return redirect(url_for('login'))
        elif not password:
            flash("Must provide password", "danger")
            return redirect(url_for('login'))

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('delight'))
        flash("Invalid username and/or password", "danger")
        return redirect(url_for('login'))

    return render_template('login.html')

#Book Now


@app.route('/booknow', methods=['GET', 'POST'])
def booknow():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        date = request.form['date']
        time = request.form['time']
        guests = request.form['guests']
        requests = request.form['requests']
        
        # Create a new reservation
        new_reservation = Reservation(name=name, email=email, phone=phone, date=date, time=time, guests=guests, requests=requests)
        
        try:
            db.session.add(new_reservation)
            db.session.commit()
            flash('Reservation successful!', 'success')
            return redirect(url_for('delight'))
        except:
            flash('There was an issue with your reservation', 'danger')
            return redirect(url_for('booknow'))
        
    
    return render_template('booknow.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Create a new contact message
        new_contact = Contact(name=name, email=email, message=message)

        try:
            db.session.add(new_contact)
            db.session.commit()
            flash('Message sent successfully!', 'success')
            return redirect(url_for('contact'))
        except:
            flash('There was an issue with your message', 'danger')
            return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.route('/delight')
def delight():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('delight.html')

@app.route('/menu')
def menu():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('MENU/DDDMenu.html')

@app.route('/menu-table')
def menu_table():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('MENU/MENU_TABLE.html')

@app.route('/drinks')
def drinks():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('MENU/DESERTS&DRINKS/Drinks.html')

@app.route('/happy-hours')
def happy_hours():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('MENU/DESERTS&DRINKS/HappyHours.html')

@app.route('/dessert')
def dessert():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('MENU/DESERTS&DRINKS/Dessert_1.html')




@app.route('/india-cuisine')
def india_cuisine():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('MENU/INDIA/India_Cuisine.html')

@app.route('/french-cuisine')
def french_cuisine():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('MENU/FRANCE/French_Cuisine.html')

@app.route('/spain-cuisine')
def spain_cuisine():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('MENU/SPAIN/Spain_Cuisine.html')

@app.route('/italy-cuisine')
def italy_cuisine():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('MENU/ITALY/Italy_Cuisine.html')

@app.route('/china-cuisine')
def china_cuisine():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('MENU/CHINA/China_Cuisine.html')

@app.route('/japan-cuisine')
def japan_cuisine():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('MENU/JAPAN/Japan_Cuisine.html')

@app.route('/korea-cuisine')
def korea_cuisine():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('MENU/KOREA/Korea_Cuisine.html')

@app.route('/australia-cuisine')
def australia_cuisine():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('MENU/AUSTRALIA/Australia_Cuisine.html')

# Add more routes as needed


#ABCD
@app.route('/about')
def about():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('ABCD/About.html')

#ABCD
@app.route('/reserve')
def reserve():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('ABCD/Reservation.html')

@app.route('/service')
def service():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('ABCD/Services.html')



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)