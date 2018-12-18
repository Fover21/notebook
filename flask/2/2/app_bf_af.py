from flask import Flask,request,session,render_template,redirect,url_for,send_file
import setting
from serv import users
app = Flask(__name__,template_folder="temp",static_folder="jingtaiwenjianmulu",static_url_path="/static")
app.config.from_object(setting.Debug)

app.register_blueprint(users.users_blue)

@app.before_request
def is_login():
    print("be1")
    if request.path == "/login":
        return None
    if session.get("user"):
        return None
    else:
        return redirect("/login")
    
@app.before_request
def be2():
    print("be2")
    return None

@app.before_request
def be3():
    print("be3")
    return None




@app.after_request
def af3(res):
    print("af3")
    return res

@app.after_request
def af2(res):
    print("af2")
    return res

@app.after_request
def af1(res):
    print("af1")
    return res




@app.route("/",endpoint="index",methods=["POST","GET"])
def index(): # wai(index) -> neibuhanshu -> () endpoint 默认视图函数名
    return render_template("index.html")

@app.route("/detail",endpoint="detail")
def detail(): # wai(detail) -> neibuhanshu -> ()
    return render_template("detail.html")


@app.route("/login",methods=["GET","POST"],strict_slashes=False)
def login():
    if request.method == "GET" :
        return render_template("login.html")
    else:
        session["user"] = request.form.get("username")
        return redirect("/")

@app.errorhandler(404)
def error404(args):
    print(args)
    return "您访问的页面不存在或者走丢了,,,,,,%s"%(args)

if __name__ == '__main__':
    app.run(debug=True)
