# @ Time    : 2020/11/23 20:01
# @ Author  : JuRan

# class A:
#     pass
# a = A()
# print(id(a))
# b = A()
# print(id(b))
# import functools
#
#
# def login_required(func):
#     # 不修改原有的函数的属性
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         pass
#
#     return wrapper
#
#
# @login_required
# def demo():
#     """demo doc"""
#     pass
#
#
# print(demo.__name__)
# print(demo.__doc__)


from qiniu import Auth, put_file, etag
import qiniu.config
'''
# 需要填写你的 Access Key 和 Secret Key
access_key = 'Pq9naz_G-zMSGq0SzRkKgb9au1puctwOTzJ9yHqo'
secret_key = 'jvgL4iJl45XhSIFzieZPlS4rNwPOIBKOhwvps2mO'
# 构建鉴权对象
q = Auth(access_key, secret_key)
# 要上传的空间
bucket_name = 'home-image-flask'
# 上传后保存的文件名
# key = 'my-python-logo.png'
# 生成上传 Token，可以指定过期时间等
token = q.upload_token(bucket_name, None, 3600)
# 要上传文件的本地路径
localfile = './2.png'
ret, info = put_file(token, None, localfile)
print(ret)
print("-"*50)
print(info)
# assert ret['key'] == key
# assert ret['hash'] == etag(localfile)
'''
"""
{#                              <option value="1">东城区</option>#}
{#                              <option value="2">西城区</option>#}
{#                              <option value="3">朝阳区</option>#}
{#                              <option value="4">海淀区</option>#}
{#                              <option value="5">昌平区</option>#}
{#                              <option value="6">丰台区</option>#}
{#                              <option value="7">房山区</option>#}
{#                              <option value="8">通州区</option>#}
{#                              <option value="9">顺义区</option>#}
{#                              <option value="10">大兴区</option>#}
{#                              <option value="11">怀柔区</option>#}
{#                              <option value="12">平谷区</option>#}
{#                              <option value="13">密云区</option>#}
{#                              <option value="14">延庆区</option>#}
{#                              <option value="15">石景山区</option>#}
{#                              <option value="16">门头沟区</option>#}
"""

"""
 <script type="text/html" id="swiper-houses-tmpl">
                {{ each houses as house }}
                 <div class="swiper-slide">
                    <a href="/detail.html?id={{ house.house_id }}"><img src="{{ house.img_url }}"></a>
                    <div class="slide-title">{{ house.title }}</div>
                </div>
                {{ /each }}
            </script>
"""

