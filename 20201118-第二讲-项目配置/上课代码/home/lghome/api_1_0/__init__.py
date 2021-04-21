# @ Time    : 2020/11/16 22:00
# @ Author  : JuRan
from flask import Blueprint

api = Blueprint('api_1_0', __name__, url_prefix='/api/v1.0')    # 创建一个蓝图对象 并设置了前缀

from . import dmeo