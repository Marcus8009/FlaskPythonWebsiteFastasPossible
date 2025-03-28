from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", name = "Marcus")

@views.route("/profile")
def profile():
    return render_template("profile.html")

# #http://127.0.0.1:8000/views/profile/superman
# @views.route("/profile")
# def profile():
#     args = request.args
#     name = args.get('name')
#     return render_template("profile.html", name=name)

@views.route("/json")
def get_json():
    return jsonify({'name':'marcus',"coolness":10})

#access json data from a route
@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))

@views.route("/go-to-json")
def go_to_json():
    return redirect(url_for("views.get_json"))

@views.route("/nothome")
def nothome():
    return "this is the nothomehome page"