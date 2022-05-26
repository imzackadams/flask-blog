from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "7704b9726481865dbd0ad45c53c6b7c5"

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


if __name__ == "__main__":
    app.run(debug=True)
