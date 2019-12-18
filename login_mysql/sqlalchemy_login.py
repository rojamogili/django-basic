
from flask import Flask, render_template, request, redirect, url_for,flash
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://roja:nani@localhost/login'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class user(db.Model):
    __tablename__="users"
    email=db.Column(db.String(50), primary_key=True)
    fname=db.Column(db.String(50), unique=False)
    lname=db.Column(db.String(50), unique=False)
    password=db.Column(db.String(50), unique=True)
    
    def __init__(self, email, fname, lname, password):
        self.email=email
        self.fname=fname
        self.lname=lname
        self.password=password


@app.route('/app/login.html')
def login():
    return render_template("login.html")

@app.route('/app/login.html',methods=["POST"])
def login_page():
    name=request.form["username"]
    pa=request.form["password"]
    p=user.query.filter(user.email==name and user.password==pa).first()
    
    if p!=None:
        #print("success")
        return "<body style='background:cyan'><h2 align='center' > you successfully login<h2></body>" 
    return render_template("login.html",error="Invalid username or password")


@app.route('/app/success_login.html')
def login_success():
    return render_template('success_login.html')

@app.route('/app/signin.html')
def register():
    return render_template('signin.html')

@app.route('/app/signin.html', methods=["POST"])
def register_page():
    email=request.form["email"]
    fname=request.form["Fname"]
    lname=request.form["Lname"]
    pa=request.form["password"]
    if email!="":
        #print(val)
        ex=user(email, fname, lname, pa)
        db.session.add(ex)
        db.session.commit()
        
        return "<body style='background:cyan'><h2 align='center'>Successfully submitted</h2></body>"
    
    return render_template('signin.html',error="Please enter details")

app.run()