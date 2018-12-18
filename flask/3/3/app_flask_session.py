from flask import Flask,request,render_template,redirect,url_for,session
from flask import views
from redis import Redis

from flask_session import Session

app = Flask(__name__)  # type:Flask
app.config["SESSION_TYPE"] = "redis"
app.config["SESSION_REDIS"] = Redis("127.0.0.1",6379,db=7)

Session(app)

@app.route("/")
def index():
    session["user"] = "JWB"
    # 87fd0ba1-6c36-44be-bc36-2a95b764e122
    return "123"

class LoginClass(views.MethodView):
    
    def get(self):
        return render_template("login.html")
    
    def post(self):
        return "123"

app.add_url_rule("/login",view_func=LoginClass.as_view("login"))



if __name__ == '__main__':
    app.run(debug=True)