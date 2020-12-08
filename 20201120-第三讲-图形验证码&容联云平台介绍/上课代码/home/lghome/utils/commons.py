# @ Time    : 2020/11/18 21:04
# @ Author  : JuRan

from werkzeug.routing import BaseConverter


class ReConverter(BaseConverter):
    def __init__(self, map, regex):
        super().__init__(map)
        # super(ReConverter, self).__init__(map)
        self.regex = regex
