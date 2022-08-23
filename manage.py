from flask import *
from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager, Server

import config
from app import create_app, db
from app.model import User
app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

manager.add_command("runserver", Server(
    use_debugger=True,
    use_reloader=True,
    host='0.0.0.0',
    port=5000)
)

# 上下文处理器，定义用户当前是否登录状态，全局可访问
@app.context_processor
def login_statue():
    # 获取session中的userna
    username = session.get('username')
    # 如果username不为空，则已登录，否则没有登录
    if username:
        try:
            # 登录后，查询用户信息并返回用户信息
            user = User.query.filter(User.username == username).first()
            if user:
                return {"username": username, 'name': user.name, 'password': user.password}
        except Exception as e:
            return e
    # 如果没有登录，返回空
    return {}

# 404页面
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# 500页面
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('404.html'), 500


if __name__ == '__main__':
    # app.run(debug=True, port="65534", host="0.0.0.0")
    manager.run()

    # python manage.py runserver -h 0.0.0.0 -p 65534
