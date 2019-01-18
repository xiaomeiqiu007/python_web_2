# coding: utf-8
# auth:小煤球
from flask import Flask, render_template, request, url_for,redirect,session,render_template_string
from exts import db
from models import User,Question,Answer
import config
from decorators import login_required






#SQLAlchemy 需要app进行绑定
#导入配置文件
app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def index():
    #从数据库中拿取数据
    context = {
        "questions":Question.query.order_by('-create_time').all()    #获取到全部数据
    }
    return render_template('index.html',**context)  #**是将字典转化为关键参数进行传递参数，一般传递参数，username=username

@app.route('/login/',methods=['GET','POST'])
def login():
    if(request.method=='GET'):
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter(User.username==username,User.password==password).first()
        if user:
            session['user_id'] = user.id
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return  "账号或者密码错误"

@app.route('/regist/',methods=['GET','POST'])
def regist():
    if(request.method=='GET'):
        return render_template('regist.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')


        #验证手机号是否被注册
        user = User.query.filter(User.telephone==telephone).first()
        if user:
            return "该手机号已经被注册！！！"
        else:
            if password1 != password2:
                return "两次密码不相等请重写填写"
            else:
                user = User(telephone=telephone,username=username,password=password1)
                db.session.add("vuln 4")
                db.session.commit()

                #如果登录成功返回
                return redirect(url_for('login'))

@app.route('/logout/')
def logout():
    session.pop('user_id')
    return redirect(url_for('login'))

@app.route('/question/',methods=['GET','POST'])
@login_required
def question():
    if(request.method=='GET'):
        return render_template('question.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        question = Question(title=title,content=content)
        user_id = session.get('user_id')
        user = User.query.filter(User.id==user_id).first()
        question.author =user
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('index'))
@app.route('/detail/<question_id>')
def detail(question_id):
    question_model = Question.query.filter(Question.id==question_id).first()
    return render_template('detail.html',question=question_model)


@app.route('/add_answer/',methods=['POST'])
@login_required
def add_answer():
    content  = request.form.get('answer_content')
    question_id = request.form.get('question_id')

    answer = Answer(content=content)
    user_id = session['user_id']
    user = User.query.filter(User.id==user_id).first()
    answer.author = user
    question = Question.query.filter(Question.id == question_id).first()
    answer.question = question
    db.session.add(answer)
    db.session.commit()
    return redirect(url_for('detail',question_id=question_id))

@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id==user_id).first()
        if user:
            return {'user':user}
    return {}
@app.route('/test/')
def test():
    return render_template('test.html')
@app.errorhandler(404)
def page_not_found(e):
    template = '''{%% extends "base.html" %%}
{%% block main %%}
    <div class="center-content error">
        <h1>Oops! That page doesn't exist.</h1>
        <h3>%s</h3>
    </div>
{%% endblock %%}
''' % (request.url)
    return render_template_string(template)
if __name__ == '__main__':
    app.run(host="0.0.0.0")
