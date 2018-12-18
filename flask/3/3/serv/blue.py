from flask import Blueprint,Flask

blue_blue = Blueprint("blue",__name__,template_folder="temp",static_folder="",static_url_path="",url_prefix="/ppp") # type:Flask


@blue_blue.route("/blue",methods=["POST","GET"])
def blues():
    return "123"