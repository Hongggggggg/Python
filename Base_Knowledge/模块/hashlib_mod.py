import hashlib
m = hashlib.md5()#
#m = hashlib.sha1()
#m = hashlib.sha256()

m.update(b'hello world')#只能接受byte类型

print(m.hexdigest())

m = hashlib.md5(b'Hello World')

print(m.hexdigest())
