
from flask import Blueprint

# 创建蓝图
admin = Blueprint("admin", __name__, url_prefix='/admin')
blog = Blueprint("blog", __name__, url_prefix='/main')

from .index import *
from .blog import *

