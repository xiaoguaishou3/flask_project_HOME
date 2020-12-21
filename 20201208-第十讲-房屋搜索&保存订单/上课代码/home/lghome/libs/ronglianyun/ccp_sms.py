# @ Time    : 2020/11/20 22:03
# @ Author  : JuRan

from ronglian_sms_sdk import SmsSDK
import json

accId = '8a216da8762cb457017679db59e71ee1'      # 容联云通讯分配的主账号ID
accToken = '3e1801e3ba494a29863c83127540bdfb'   # 容联云 主账号TOKEN
appId = '8a216da8762cb457017679db5af91ee8'      # 容联云分配应用ID


def send_message():
    sdk = SmsSDK(accId, accToken, appId)
    tid = '1'  # 短信模板ID 测试1
    mobile = '13928646499'
    # datas  验证码   过期时间 单位是分钟
    datas = ('1234', '5')
    resp = sdk.sendMessage(tid, mobile, datas)
    result = json.loads(resp)
    print(result)


class CCP(object):
    """发送短信的单例类"""
    # _instance = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.sdk = SmsSDK(accId, accToken, appId)
        return cls._instance

    def send_message(self, mobile, datas, tid):
        sdk = self._instance.sdk
        # sdk = self.sdk
        # tid = '1'
        # mobile = '18646175116'
        # datas  验证码   过期时间 单位是分钟
        # datas = ('1234', '5')
        resp = sdk.sendMessage(tid, mobile, datas)
        result = json.loads(resp)
        if result['statusCode'] == '000000':
            return 0
        else:
            return -1


if __name__ == '__main__':
    send_message()
    # c = CCP()
    # c.send_message('18646175116', ('1234', '5'), 1)

