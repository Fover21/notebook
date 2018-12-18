from flask import Flask,render_template,redirect,jsonify,send_file,request,Markup,session
app = Flask(__name__)

app.secret_key = "yinjiaodawangba"

STUDENT = {'name': 'Old', 'age': 38, 'gender': '中'}

STUDENT_LIST = [
    {'name': 'Old', 'age': 38, 'gender': '中'},
    {'name': 'Boy', 'age': 73, 'gender': '男'},
    {'name': 'EDU', 'age': 84, 'gender': '女'}
]

STUDENT_DICT = {
    1: {'name': 'Old', 'age': 38, 'gender': '中'},
    2: {'name': 'Boy', 'age': 73, 'gender': '男'},
    3: {'name': 'EDU', 'age': 84, 'gender': '女'}
}

@app.template_global()
def ab(a,b):
    return a+b

@app.template_filter()
def axb(a,b):
    return a*b

@app.route("/")
def index():
    inp = Markup("<input type='text'>")
    if session.get("user"):
        print(session)
        # return json.dumps({"name":"JWB","age":73})
        # return jsonify({"name":"JWB","age":73})
        return render_template("index.html",stu=STUDENT_DICT,inp=inp)
    
    return redirect("/login")


@app.route("/bl")
def bl():
    # return json.dumps({"name":"JWB","age":73})
    # return jsonify({"name":"JWB","age":73}
    
    return render_template("my_block.html", stu=STUDENT_DICT)


@app.route("/login",methods=("GET","POST"))
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        user_info = request.form.to_dict()
        if user_info.get("username") == "JWB" and user_info.get("pwd") == "DSB":
            session["user"] = user_info.get("username")
            return redirect("/")
        else:
            return render_template("login.html",msg="用户名密码错误")
        
    

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=9527,debug=True)


# eyJ1c2VyIjoiSldCIn0.DvS9eg.aXNffcXrztlPEzfR8ulOlU3Xbww
# .eJyrViotTi1SslLyCndS0gFzDFF4Rig8YxSeCQrPFMqrBQDoaBcs.DvS9vQ.sW0iFbfMJmAz8kOZJ36aWRclY0c
# .eJxFTTsSAiEMvYpDbUFCwsfS0gvY0MDCHkCHyvHuJsjONm9e8n4fM979ZW7m8byb6zxArjwYKAp2aIIINQ_qUE4X_jP6RrEky24p7lB8wCJhR2UpdGY2VRIm5XaW26RD1i8vH97gp7e1LpwrCt9tuUh99ZRHrG2OBJCPRRZeOWphAUWS8pC2OcG7-f4AmopIXQ.DvS-LA.lrKb_t7s7TVnDlwICSYEANSonJ8