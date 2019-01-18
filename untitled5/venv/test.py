# coding: utf-8
# auth:小煤球
def login(func):
    def regist():
        print 'tiis is regist'
        func()
    return regist

@login
def run():
    print "this is run"
run()

#首先执行run(),相当于执行run=login（run）=regist，所以就会变成regist（）
#所以会执行regist函数，接着因为传的是函数名，返回的也是函数，在函数内部func=run。
#所以会执行run（），故输出this is run
