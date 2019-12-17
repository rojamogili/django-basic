# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 22:45:34 2019

@author: ROJA MOGILI
"""
from flask import Flask, render_template, request, redirect, url_for,flash
import mysql.connector;
mydb=mysql.connector.connect(host="localhost", user="roja", passwd="nani", database="login")
db=mydb.cursor()

app=Flask(__name__)

@app.route('/app/login.html')
def login():
    return render_template("login.html")

@app.route('/app/login.html',methods=["POST"])
def login_page():
    name=request.form["username"]
    pa=request.form["password"]
    n=(name, )
    db.execute("select password from user_details where email= %s", n)
    p=db.fetchall()
    if pa==p[0][0]:
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
        val=(email, fname, lname, pa)
        #print(val)
        
        db.execute("insert into user_details (email, fname, lname, password) values(%s, %s, %s, %s)", (val))
        mydb.commit()
        
        return "<body style='background:cyan'><h2 align='center'>Successfully submitted</h2></body>"
    
    return render_template('signin.html',error="Please enter details")
app.run()