from flask import Flask,request,render_template
from flask import views
from wtforms.fields import simple,core
from wtforms import Form
from wtforms import validators
# from wtforms import widgets

class LoginForm(Form):
    username = simple.StringField(
        label="用户名",
        validators=[
            validators.DataRequired(message="不能为空"),
            validators.Length(min=3,max=5,message="不能小于3位，不能大于5位")
        ],
        # widget=widgets.TextInput(),
        render_kw={"class":"my_username"}
    )

    password = simple.PasswordField(
        label="密码",
        validators=[
            validators.DataRequired(message="不能为空"),
            validators.Length(min=6, max=6, message="密码必须为6位"),
            validators.Regexp(regex="\d+", message="密码必须位数字"),
        ],
        # widget=widgets.TextInput(),
        render_kw={"class": "my_password"}
    )
    
    
class RegForm(Form):
    username = simple.StringField(
        label="用户名",
        validators=[
            validators.DataRequired(message="不能为空"),
            validators.Length(min=3, max=5, message="不能小于3位，不能大于5位")
        ],
        # widget=widgets.TextInput(),
        render_kw={"class": "my_username"}
    )

    nickname = simple.StringField(
        label="昵称",
        validators=[
            validators.DataRequired(message="不能为空"),
        ],
        # widget=widgets.TextInput(),
        render_kw={"class": "my_username"}
    )
    
    password = simple.PasswordField(
        label="密码",
        validators=[
            validators.DataRequired(message="不能为空"),
            validators.Length(min=6, max=6, message="密码必须为6位"),
            validators.Regexp(regex="\d+", message="密码必须位数字"),
        ],
        # widget=widgets.TextInput(),
        render_kw={"class": "my_password"}
    )

    repassword = simple.PasswordField(
        label="重复密码",
        validators=[
            validators.EqualTo(fieldname="password",message="两次密码不一致")
        ]
    )

    email = simple.StringField(
        label="昵称",
        validators=[
            validators.Email(message="格式不正确"),
        ],
        # widget=widgets.TextInput(),
        render_kw={"class": "my_username"}
    )
    
    gender = core.RadioField(
        label="性别",
        coerce=int,
        choices=(
            (1,"女"),
            (2,"男")
        ),
        default=1
    )
    
    hobby = core.SelectMultipleField(
        label="爱好",
        coerce=int,
        choices=(
            (1, "小姐姐"),
            (2, "小萝莉"),
            (3, "小哥哥"),
            (4, "小正太"),
            (5, "阿姨"),
            (6, "大叔"),
        ),
        default=(1,2,5)
    )
    
    submit = simple.SubmitField(
        label="提交"
    )
    


app = Flask(__name__)  # type:Flask


@app.route("/")
def index():
    # 87fd0ba1-6c36-44be-bc36-2a95b764e122
    return "123"

class LoginClass(views.MethodView):
    
    def get(self):
        lf = LoginForm()
        return render_template("login.html",lf=lf)
    
    def post(self):
        lf = LoginForm(request.form)
        if lf.validate():
            return "123"
        else:
            return render_template("login.html", lf=lf)

app.add_url_rule("/login",view_func=LoginClass.as_view("login"))


class RegClass(views.MethodView):
    
    def get(self):
        rf = RegForm()
        return render_template("reg.html", rf=rf)
    
    def post(self):
        rf = RegForm(request.form)
        if rf.validate():
            return "123"
        else:
            return render_template("reg.html", rf=rf)


app.add_url_rule("/reg", view_func=RegClass.as_view("reg"))


if __name__ == '__main__':
    app.run(debug=True)