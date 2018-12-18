from flask import Flask,request,session,render_template,redirect,url_for,send_file
import setting
app = Flask(__name__,template_folder="temp",static_folder="jingtaiwenjianmulu",static_url_path="/static")
# app.secret_key = "jinwangbaMD5de"
# app.config["SECRET_KEY"] = "jinwangbaMD5de"
# app.config
# app.session_cookie_name = "qishiwoyebuzhidaozheshishenmedongxi"

app.config.from_object(setting.Debug)
# app.config.from_object(setting.XianShang)
# app.config.from_object(setting.Testing)

def wai(func):
    def neibuhanshu(*args,**kwargs):
        if session.get("user"):
            ret = func(*args,**kwargs)
            return ret
        else:
            return redirect("/login")
    return neibuhanshu

# @app.route("/static/<filename>")
# def get_static(filename):
#     # falsk -> static_folder ->
#     return send_file("statics/" + filename)


@app.route("/<nid>",endpoint="index",methods=["POST","GET"])
# @wai
def index(nid): # wai(index) -> neibuhanshu -> () endpoint 默认视图函数名
    # print(url_for("neibuhanshu"))
    # print(url_for("neibuhanshu"))
    # print(url_for("qishijiushiyigexiangxiyemian"))
    # print(nid)
    return render_template("index.html")

@app.route("/detail",endpoint="detail")
# @wai
def detail(): # wai(detail) -> neibuhanshu -> ()
    return render_template("detail.html")


@app.route("/login",methods=["GET","POST"],strict_slashes=False)
def login():
    if request.method == "GET" :
        return render_template("login.html")
    else:
        session["user"] = request.form.get("username")
        return redirect("/")





if __name__ == '__main__':
    app.run(debug=True)
    