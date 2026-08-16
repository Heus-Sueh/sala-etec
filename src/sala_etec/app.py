from flask import Flask, render_template, request

app = Flask(__name__)


def main() -> None:
    print("Hello from sala-etec!")
    app.run(debug=True)


@app.route("/")
def root():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def save():
    name = request.form.get("name")
    password = request.form.get("password")
    # return f"Your username is {name} and password is {password}"
    return render_template("home.html", user=name)


if __name__ == "__main__":
    main()
