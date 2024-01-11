from service.handle_image import download_image, get_hash_value, get_size_value, change_url
import base64
import hashlib
import time

url = 'http://wx.qlogo.cn/mmopen/x9yFCw0S2sDss2r593feziccLDM2tiaDRM8gCzHuL7C/64'
url = change_url(url)
print(url)

data = '4397977436160_22_5Yqf5Yqz'
md5 = hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
print(md5)


time_str = time.strftime("%Y-%m-%d %H:%M:%S")
print(time_str)

url = 'http://wx.qlogo.cn/mmopen/x9yFCw0S2sDss2r593feziccLDM2tiaDRM8gCzHuL7CC85dKCwdhXYOghtbmwcfG9T7e0MtpUg4e11CtW3sXZQ2zXc6W1IWPLF/64'

try:
    url = change_url(url)
    local_path = 'data/image'
    local_file = download_image(url, local_path)
    head_id, head_size = get_hash_value(local_file, (6, 7))

except:
    head_id = 0
    head_size = 0

print(head_id)
print(head_size)

name = '老李'
base64_name = str(base64.b64encode(name.encode('utf-8')), 'utf-8')
print(base64_name)

name = '老杨'
base64_name = str(base64.b64encode(name.encode('utf-8')), 'utf-8')
print(base64_name)

print(str(base64.b64decode(base64_name), 'utf-8'))


name = ' '
base64_name = str(base64.b64encode(name.encode('utf-8')), 'utf-8')
print(base64_name)

name = '  '
base64_name = str(base64.b64encode(name.encode('utf-8')), 'utf-8')
print(base64_name)
