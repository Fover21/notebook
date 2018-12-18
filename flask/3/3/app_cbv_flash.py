from flask import Flask,request,render_template,redirect,url_for,flash,get_flashed_messages
from flask import views

app = Flask(__name__)  # type:Flask
app.secret_key = "123"

@app.route("/")
def index():
    # flash("6666","tag")
    # flash("7777","tags")
    return "123"

class LoginClass(views.MethodView):
    
    def get(self):
        # print(get_flashed_messages("tag"))
        # print(get_flashed_messages())
        print(url_for("login"))
        return render_template("login.html")
    
    def post(self):
        return "123"
    
# self.add_url_rule(rule, endpoint, f, **options)

app.add_url_rule("/login",view_func=LoginClass.as_view("login"))

@app.before_first_request
def asd():
    return "123"


if __name__ == '__main__':
    app.run(debug=True)