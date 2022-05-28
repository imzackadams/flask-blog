from flask import  render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

# dummy data
blog = [
    {
        "author": "Zack Adams",
        "title": "Blog Post 1",
        "content": "First Content",
        "date_posted": "April 20,2022"
    },
    {
        "author": "Zack Adams",
        "title": "Blog Post 2",
        "content": "Second Content",
        "date_posted": "May 28,2022"
    }
]


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', posts=blog)


@app.route("/about")
def about():
    return render_template('about.html', title="about")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for('index'))
    # debug purpose
    # else:
    #     flash("Failed validation")
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == "password":
            flash("You have been logging in!", "success")
            return redirect(url_for("index"))
        else:
            flash("Login unsuccessful. Please check username and password", "danger")
    return render_template("login.html", title="Login", form=form)

