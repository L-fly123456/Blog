import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    # DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    WTF_CSRF_CHECK_DEFAULT = False
    # QLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    a = os.environ
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:L_fly1335108246@localhost:3306/blog?charset=utf8mb4"
    ARTICLES_PER_PAGE = 10
    COMMENTS_PER_PAGE = 6
    SECRET_KEY = 'secret key to protect from csrf'
    # WTF_CSRF_SECRET_KEY = 'random key for form' # for csrf protection
    # Take good care of 'SECRET_KEY' and 'WTF_CSRF_SECRET_KEY', if you use the
    # bootstrap extension to create a form, it is Ok to use 'SECRET_KEY',
    # but when you use tha style like '{{ form.name.labey }}:{{ form.name() }}',
    # you must do this for yourself to use the wtf, more about this, you can
    # take a reference to the book <<Flask Framework Cookbook>>.
    # But the book only have the version of English.

    # 更换session保存路径
    # SESSION_TYPE = 'filesystem'
    # SESSION_FILE_DIR = 'D:\\Project\\Blog\\flask_session'
    # SESSION_FILE_THRESHOLD = 10  # 默认是500,大于设定值,会自动删除
    # SESSION_FILE_MODE = 600  # 默认值,文件模式,读写执行
    # SESSION_PERMANENT = False
    # SESSION_USE_SIGNER = True  # 加密
    # SESSION_KEY_PREFIX = 'session'

    @staticmethod
    def init_app(app):
        pass

