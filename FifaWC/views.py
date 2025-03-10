from flask import Blueprint, render_template, request

views = Blueprint(__name__, "views")

@views.route("/", methods = ["GET", "POST"])
def home():
    search_result=None
    if request.method == "POST":
        user_query = request.form.get("query")
        search_result = f"You searched for: {user_query}"
    return render_template("index.html", search_result=search_result)