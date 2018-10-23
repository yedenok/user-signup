from flask import Flask, request, render_template, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['get'])
def index():
    return render_template("login.html")

@app.route("/", methods=['post'])
def verify():
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['verify_password']
    email = request.form['email']
    username_error = ''
    password_error = ''
    confirm_password_error = ''
    email_error = ''
    if username == "":
        username_error = "Please enter a username"
    elif len(username) < 3 or len(username) > 20:
        username_error = "Username must be between 3 and 20 characters"
    if password == "":
        password_error = "Please enter a password"
    elif len(password) < 3 or len(password) > 20:
        password_error = "Password must be between 3 and 20 characters"
    elif password != confirm_password:
        confirm_password_error = "Passwords do not match"
    if email:
        if "@" not in email or "." not in email:
            email_error = "Email address is not valid"
    if username_error or password_error or confirm_password_error or email_error:
        return render_template("login.html", username=username, username_error=username_error,
        password=password, password_error=password_error, confirm_password_error=confirm_password_error,
        email=email, email_error=email_error)
    else: 
        return redirect("/welcome?username=" + username)


@app.route("/welcome", methods=['get'])
def welcome():
    username = request.args.get("username")
    return render_template("welcome_user.html", username=username)


app.run()

