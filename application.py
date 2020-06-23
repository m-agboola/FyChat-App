from flask import Flask, render_template, redirect, url_for

from forms import *
from models import *

# Configure app
app = Flask(__name__)
app.secret_key = "replace later"

# Configure Database
app.config['SQLALCHEMY_DATABASE_URI']='postgres://fusgwdksjiairg:b47071037d25ec1a8b90e07b1686f978a3146daa85a89ff07df315b385c9603c@ec2-35-172-73-125.compute-1.amazonaws.com:5432/dbvrf5qu42cmoq'
db = SQLAlchemy(app)

@app.route("/", methods=["GET", "POST"])
def index():
    
    reg_form = RegistrationForm()
    
    # Update database if validation was successful
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data
        
        # Add user to DB
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('login'))
        
    return render_template("index.html", form=reg_form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    
    login_form = LoginForm()
    
    #Allow login if validation successful
    if login_form.validate_on_submit():
        return "Logged in, finally!"
    
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.debug = True
    app.run()