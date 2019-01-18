# coding: utf-8
# auth:小煤球
#登录限制装饰器
from functools import wraps
from flask import  session,redirect,url_for
def login_required(func):
    @wraps(func)    #返回函数的真实名字让index.__name__=index
    def wapper(*args,**kwargs):   #表示接受任何参数
        if session.get('user_id'):
            return func(*args,**kwargs)   #返回index（）执行结果
        else:
            return redirect(url_for('login'))
    return wapper
