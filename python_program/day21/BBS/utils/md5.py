#自定义一个加密函数，给用户密码加密，因为数据库里存放的密码是密文的
def encrypt(pwd):
    import hashlib

    obj = hashlib.md5()
    obj.update(pwd.encode('utf-8'))
    data = obj.hexdigest()
    return data