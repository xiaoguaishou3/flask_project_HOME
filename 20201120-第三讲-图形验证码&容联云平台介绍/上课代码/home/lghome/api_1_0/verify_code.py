# @ Time    : 2020/11/20 20:44
# @ Author  : JuRan

from . import api
from lghome.utils.captcha.captcha import captcha
from lghome import redis_store
import logging
from flask import jsonify, make_response
from lghome import constants
from lghome.response_code import RET
"""
REST风格
goods
/add_goods
/update_goods
/delete_goods
/get_goods

goods   
请求的方式
GET     查询
POST    保存
PUT     修改
DELETE  删除
"""

# UUID image_code_id
# 时间戳+随机数
# GET 127.0.0.1/api/v1.0/image_codes/<image_code_id>
# redis中数据类型
# UUID:验证码
# hash    image_code:{id:1, name:juran}
# string  uuid:xxxx
#   set key value
#   exprie
#   setex
# 过期时间
@api.route("/image_codes/<image_code_id>")
def get_image_code(image_code_id):
    """
    获取图片验证码
    :param image_code_id: 图片的编号
    :return: 验证码,验证码图像
    """
    # 验证参数
    # 业务逻辑处理
    # 生成验证码图片
    text, image_data = captcha.generate_captcha()
    # 保存验证码
    # redis_store.set()
    # redis_store.exprie()
    try:
        redis_store.setex('image_code_%s' % image_code_id, constants.IAMGE_CODE_REDIS_EXPIRES, text)
    except Exception as e:
        logging.error(e)
        return jsonify(errno=RET.DBERR, errmsg='保存图片验证码失败')

    # 返回值
    response = make_response(image_data)
    response.headers['Content-Type'] = 'image/jpg'
    return response

