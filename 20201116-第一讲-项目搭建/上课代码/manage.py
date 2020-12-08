# @ Time    : 2020/11/16 21:19
# @ Author  : JuRan
from lghome import create_app

app = create_app('dev')


if __name__ == '__main__':
    app.run()