from flask import Flask, render_template, url_for

app = Flask(__name__)


# @app.route("/<title>")
# @app.route("/index/<title>")
# def index(title):
#     return render_template("index.html", title=title)


# @app.route("/base")
# def base():
#     return render_template("base.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/request")
def request():
    return render_template("request.html")


@app.route("/sc")
def sc():
    return render_template("sc.html")


@app.route("/warehouse")
def warehouse():
    return render_template("warehouse.html")


@app.route("/warehouseSc")
def warehousesc():
    return render_template("warehouseSc.html")


@app.route("/delivery warehouse")
def dwarehouse():
    return render_template("delivery warehouse.html")


@app.route("/log")
def log():
    return render_template("log.html")


@app.route("/statistics")
def statistics():
    return render_template("statistics.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")




# @app.route("/about")
# def about():
#     return render_template("about.html", number=5)
#
#
# @app.route("/training/<prof>")
# def train(prof):
#     return render_template("training.html", profession=prof)


if __name__ == "__main__":
    app.run(port=666, host='127.0.0.1')

# @app.route("about")
# def about(title):
#     return render_template("about.html", title=title)
#
# @app.route("/base")
# def base():
#     return render_template("base.html")