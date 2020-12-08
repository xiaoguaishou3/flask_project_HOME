# @ Time    : 2020/11/16 22:05
# @ Author  : JuRan
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect
from config import config_map


# 工厂模式
def create_app(config_name):

    app = Flask(__name__)

    # if config_name == "dev":
    #     from config import DevConfig
    #     app.config.from_object(DevConfig)
    # else:
    #     from config import ProConfig
    #     app.config.from_object(ProConfig)

    config_class = config_map.get(config_name)
    app.config.from_object(config_class)

    return app


db = SQLAlchemy(app)

# 创建Redis
redis_store = redis.Redis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

# session
Session(app)

# post请求  wtf  csrf
CSRFProtect(app)