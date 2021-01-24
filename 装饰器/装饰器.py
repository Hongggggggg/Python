account = {
    'is_authenticated' : False,#用户登录标志
    'username' : 'hong',
    'password' : '123'
}

def login(func):
    def inner(*args, **kwargs): #*args, **kwargs目的是后期可拓展func()的参数
        if account['is_authenticated'] == False:
            username = input("username: ")
            password = input("password: ")
            if(username == account['username'] and password == account['password']):
                account['is_authenticated'] = True
                print("login success")
                func(*args, **kwargs)
            else:
                print('username or password is wrong!')
        else:
            func(*args, **kwargs)
    return inner


@login #语法糖，装饰器，可有多个装饰器按先后循序执行
def normal():
    print("Normal")


@login
def vip(level):
    if level > 5:
        print("高级VIP")
    else:
        print("普通vip")


normal()
vip(6)
