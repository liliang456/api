from flask import Flask, jsonify
from flask import request
from common.mysql_operate import db


app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
data = [
    {"id": 1, "username": "小明", "password": "123456", "role": 0, "sex": 0, "telephone": "10086", "address": "北京市海淀区"},
    {"id": 2, "username": "李华", "password": "abc", "role": 1, "sex": 0, "telephone": "10010", "address": "广州市天河区"},
    {"id": 3, "username": "大白", "password": "666666", "role": 0, "sex": 1, "telephone": "10000", "address": "深圳市南山区"},
    {"id": 4, "username": "大白", "password": "666666", "role": 0, "sex": 1, "telephone": "10000", "address": "南京市中山区"},
]

@app.route("/users", methods=["GET"])
def get_all_users():
    """获取所有用户信息"""
    sql = "select * from user"
    data = db.select_db(sql)
    return jsonify({"code": "0", "data": data, "msg": "操作成功"})

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    """获取某个用户信息"""
    if user_id > 0 and user_id <= len(data):
        return jsonify({"code": "0", "data": data[user_id - 1], "msg": "操作成功"})
    return jsonify({"code": "1", "msg": "用户不存在"})

@app.route("/user/<string:username>",methods=["GET"])
def get_username(username):
    sql = "select * from user where username='{}'".format(username)
    data = db.select_db(sql)
    if data:
        return jsonify({"code":"0","data":data,"msg":"查询成功"})
    return jsonify({"code":"1004","msg":"查询不到相关信息"})

@app.route("/register",methods=["POST"])
def user_register():
    username = request.form.get("username").strip()
    print('----------',username)
    password = request.form.get("password").strip()
    sex = request.form.get("sex","0").strip()
    telephone = request.form.get("telephone","").strip()
    print('----------',telephone)
    address = request.form.get("address","")
    if username and password and sex:
        import re
        sql1 = "select username from user where username='{}'".format(username)
        uname = db.select_db(sql1)
        sql2 = "select telephone from user where telephone='{}'".format(telephone)
        tphone = db.select_db(sql2)
        if uname:
            return jsonify({"code":2002,"msg":"该用户名已存在"})
        elif not (sex == "0" or sex == "1"):
            return jsonify({"code":2003,"msg":"性别只能输入0或者1"})
        elif not (len(telephone)) == 11 and re.match("^1[3,5,7,8]\d{9}$", telephone):
            return jsonify({"code":2004,"msg":"请输入11位的手机号码"})
        elif tphone:
            return jsonify({"code": 2005, "msg": "手机号已被注册！！！"})
        else:
            sql3 = "insert into user(username, password, role, sex, telephone, address)" \
                   "values('{}', '{}', '1', '{}', '{}', '{}')".format(username, password, sex, telephone, address)
            db.execute_db(sql3)
            print("新增用户信息 ==>> {}".format(sql3))
            return jsonify({"code": 0, "msg": "注册成功"})
    else:
        return jsonify({"code":2000,"msg":"输入不全"})


@app.route("/login",methods=['POST'])
def user_login():
    username = request.values.get("username")
    password = request.values.get("password")
    if username and password:
        sql1 = "SELECT username FROM user WHERE username = '{}'".format(username)
        res1 = db.select_db(sql1)
        # print("查询到用户名 ==>> {}".format(res1))
        if not res1:
            return jsonify({"code": 1003, "msg": "用户名不存在！！！"})
        sql3 = "SELECT password FROM user WHERE password = '{}'".format(password)
        pwd = db.select_db(sql3)
        if not pwd:
            return jsonify({"code": 1004, "msg": "密码不存在！！！"})
        sql2 = "select * from user where username='{}' and password = '{}'".format(username,password)
        res2 = db.select_db(sql2)
        if res2:
            return jsonify({"code":0,"msg":"恭喜登录成功"})
    else:
        return jsonify({"code":1000,"msg":"登录名或密码不能为空"})






if __name__ == '__main__':
    app.run(debug=True)