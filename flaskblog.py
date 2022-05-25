from flask import Flask, render_template, url_for

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=True)
