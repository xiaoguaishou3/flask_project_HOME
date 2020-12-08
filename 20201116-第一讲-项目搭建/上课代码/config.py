# @ Time    : 2020/11/16 21:47
# @ Author  : JuRan
import redis


class Config(object):
    """配置信息"""

    SECRET_KEY = 'ASDAXCWE5ERTFG%%DAS34'  # 加盐加密法
    USERNAME = 'root'
    PASSWORD = 'root'
    HOSTNAME = '127.0.0.1'
    PORT     = 3306
    DATEBASE = 'home'

    # redis配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # flask-session
    # 将 session 保存在redis中
    SESSION_TYPE = 'redis'

    SESSION_REDIS = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
    # 是否对会话进行签名
    SESSION_USE_SIGNER = True
    # 存活时间
    PERMANENT_SESSION_LIFETIME = 8640   # 单位是秒

    # 数据库
    DB_URL = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATEBASE)


class DevConfig(Config):
    """开发环境"""
    DEBUG = True


class ProConfig(Config):
    """生产环境"""


config_map = {
    'dev': DevConfig,
    'pro': ProConfig
}
