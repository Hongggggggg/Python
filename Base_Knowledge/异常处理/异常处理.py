try:
    num1 = int(input('n1>>'))
    num2 = int(input('n2>>'))
    print(num1 + num2)
except ValueError as e:
    print(e)


try:
    a = 0
    a.abc
except AttributeError as e:
    print(e)


try:
    print(1)
    raise IndexError #手动触发异常
except NameError as e:
    print(e)
except Exception as e:
    print('万能异常', e)

else:
    print('没发生异常')

finally:
    print('异常不异常都会走这')


class WebConnErr(BaseException):#自定义异常
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    print("Connect to Google")
    raise WebConnErr('无法翻墙访问')
except WebConnErr as e:
    print(e)
except Exception as e: #无法抓到自定义的异常
    print(e)
