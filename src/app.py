from flask import Flask,render_template,request,url_for
import pymysql.cursors
app = Flask(__name__,template_folder='templates')

# 数据库连接配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:zht281617@39.106.137.68/easychat'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def con_my_sql(query, args=None):
    connection = pymysql.connect(
        host='39.106.137.68',
        user='root',
        password='zht281617',
        database='easychat',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, args)
            result = cursor.fetchall()
            connection.commit()
        return result
    finally:
        connection.close()

@app.route("/")
def index():
    return render_template('login.html')

@app.route("/index")
def index_page():
    return render_template('index.html')

@app.route("/help")
def help_page():
    return render_template('help.html')

@app.route("/information")
def information_page():
    return render_template('information.html')

@app.route("/setting")
def settings_page():
    return render_template('setting.html')
@app.route("/login")
def login_page():
    return render_template('login.html')

@app.route("/register")
def register_page():
    return render_template('register.html')

@app.route('/login',methods=['POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        pwd = request.form['password']
        query = "SELECT * FROM users WHERE username=%s"
        cursor_select = con_my_sql(query, (name,))
        # code = "select * from users where username='%s'" % (name) # SQL语句
        # cursor_ans = con_my_sql(code) # 执行SQL语句
        # cursor_select = cursor_ans.fetchall() # 字典格式返回数据,
        if len(cursor_select) > 0: # 存在用户名
            if pwd == cursor_select[0]['password']: # 密码正确
                return render_template('index.html')
            else:
                return "密码错误"
        else: # 不存在用户名
            return "用户不存在"

@app.route('/register',methods=['POST'])
def Register():
    if request.method == 'POST':
        name = request.form['username']
        pwd = request.form['password']
        query_select = "SELECT * FROM users WHERE username=%s"
        cursor_select = con_my_sql(query_select, (name,))
        if len(cursor_select) > 0:  # 存在用户名
            return "用户已存在"
        else:
            query_insert = "INSERT INTO users (username, password) VALUES (%s, %s)"
            con_my_sql(query_insert, (name, pwd))
            return "注册成功"


if __name__ == '__main__':
    app.run(debug=True)
