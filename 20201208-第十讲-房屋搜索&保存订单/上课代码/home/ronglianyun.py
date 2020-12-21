# @ Time    : 2020/11/20 21:57
# @ Author  : JuRan

from ronglian_sms_sdk import SmsSDK

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
    print(type(resp))
    print(resp)


send_message()