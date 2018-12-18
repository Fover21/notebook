from flask import Blueprint,render_template

users_blue = Blueprint("users",__name__,template_folder="user_temp",url_prefix="/user")

@users_blue.route("/user_add") #/user/user_add
def user_add():
    return render_template("user_add.html")
