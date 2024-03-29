# @ Time    : 2020/11/18 20:51
# @ Author  : JuRan

# 提供静态文件的蓝图
from flask import Blueprint, current_app

html = Blueprint('web_html', __name__)  # 静态文件管理 favicon.ico代表图标图案

# 127.0.0.1:5000/   访问首页
# 127.0.0.1:5000/index.html   访问首页
# 127.0.0.1:5000/register.html   访问注册
# 路由转换


# 需求：当访问对应的页面时，使用相应的静态文件展示页面
# 127.0.0.1:5000/index.html
@html.route("/<re('.*'):html_file_name>")
def get_html(html_file_name):
    """提供HTML文件"""

    # 访问首页
    if not html_file_name:
        html_file_name = 'index.html'

    # 如果访问的不是favicon,再去拼接
    if html_file_name != 'favicon.ico':
        html_file_name = 'html/' + html_file_name

    return current_app.send_static_file(html_file_name)
