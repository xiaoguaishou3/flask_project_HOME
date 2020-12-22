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


# class CCP(object):
#     """发送短信的单例类"""
#     # _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, "_instance"):
#             cls._instance = super().__new__(cls, *args, **kwargs)
#             cls._instance.sdk = SmsSDK(accId, accToken, appId)
#         return cls._instance
#
#     def send_message(self, mobile, datas, tid):
#         sdk = self._instance.sdk
#         # sdk = self.sdk
#         # tid = '1'
#         # mobile = '18646175116'
#         # datas  验证码   过期时间 单位是分钟
#         # datas = ('1234', '5')
#         resp = sdk.sendMessage(tid, mobile, datas)
#         result = json.loads(resp)
#         if result['statusCode'] == '000000':
#             return 0
#         else:
#             return -1

class CCP(object):
    """51.18"""
    def __new__(cls, *args, **kwargs):
        """
        单例模式
        __new__ 在实例化对象之前执行
        hasattr() 结果返回T 或者 F
        """
        if not hasattr(cls, '_con'):
            # TODO: 这里不太理解
            cls._con = super().__new__(cls, *args, **kwargs)
            cls._con.sdk = SmsSDK(accId, accToken, appId)

        return cls._con

    def send_message(self, mobile, datas, tid):
        sdk = self._con.sdk
        self.mobile = mobile
        self.datas = datas
        self.tid = tid
        resp = sdk.sendMessage(self.tid, self.mobile, self.datas)
        result = json.loads(resp)
        print(result)


if __name__ == '__main__':
    # send_message()
    c = CCP()
    c.send_message('13527676711', ('1234', '5'), 1)

