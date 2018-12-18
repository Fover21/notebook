from flask import Flask,request,session,render_template,redirect
from serv import blue

app = Flask(__name__,template_folder="temp",static_folder="static",static_url_path="/static")  # type:Flask


class DebugSetting(object):
    DEBUG = True


app.config.from_object(DebugSetting)

app.register_blueprint(blue.blue_blue)


@app.route("/index/<s>",methods=["GET","POST"],endpoint="index",defaults={"nid":1},strict_slashes=True,redirect_to="/login")
def index(nid,s):
    return "123"
# methods=["GET","POST"] endpoint="index"
# "/index/<s>" index(s)

@app.before_request # 请求进入视图函数之前
def be1():
    return None

@app.after_request # 视图函数结束之后，返回客户端之前
def af1(response):
    return response

# be1 be2 be3 - af3 af2 af1
# be1 - af3 af2 af1






if __name__ == '__main__':
    app.run("0.0.0.0",5000,debug=True)