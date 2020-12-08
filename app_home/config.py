# @ Time    : 2020/12/5 14:34
# @ Author  : Emily
import redis

class Config(object):
    """配置信息"""

    # TODO: SECRET_KEY = 'ASDAXCWE5ERTFG%%DAS34'
    USERNAME = 'root'
    PASSWORD = 'root'
    HOSTNAME = '127.0.0.1'
    PORT = 3306
    DATEBASE = 'home'

    # redis配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # flask-session
    # TODO: 将 session 保存在redis中
    # '''待补充'''

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
