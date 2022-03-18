from flask import Flask, render_template, flash, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

import flask_wtf


app = Flask(__name__)
app.config["SECRET_KEY"] = "DJ6jt656HgFFh5"


@app.route('/', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login successful", 'success')
        return redirect(url_for("home"))
    return render_template("login.html", form=form)


@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/logout')
def logout():
    flash("You are logged out.")
    return redirect(url_for("login"))


class LoginForm(FlaskForm):
    email = StringField("Email Address", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=25)])
    submit = SubmitField("Please login")
