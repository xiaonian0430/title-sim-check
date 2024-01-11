# encoding: utf-8
"""
@author: xiao nian
@contact: xiaonian030@163.com
@date: 2022-09-08
"""
print(">> 程序启动中...")
__copyright__ = "Copyright (c) (2022-2022) QF Inc. All Rights Reserved"
__author__ = "Xiao Nian"
__date__ = "2022-09-10:14:13:24"
__version__ = "1.0.0"

from service.article import sync_title
print('>> 同步标题...')
sync_title()
print('>> 同步标题完毕')



from flask import Flask, request, json
from flask_cors import CORS
from gevent import monkey
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
from service.article import real_time_checking, get_sim_title
import threading

# 提供猴子补丁MonkeyPatch方法，通过该方法gevent能够
# 修改标准库里面大部分的阻塞式系统调用，
# 包括socket、ssl、threading和 select等模块，而变为协作式运行
monkey.patch_all()
app = Flask(__name__)
app.config.update(
    DEBUG=False
)
CORS(app, resources=r'/*')


@app.errorhandler(404)
def error(err):
    result = {"code": 404, "data": {"err": True}, "msg": 'The requested URL was not found on the server'}
    return json.dumps(result, ensure_ascii=False)


@app.route("/")
def home():
    result = {"code": 400, "data": {"empty": 0}, "msg": 'no access'}
    return json.dumps(result, ensure_ascii=False)


@app.route("/favicon.ico")
def favicon():
    result = {"code": 400, "data": {"empty": 0}, "msg": 'no access'}
    return json.dumps(result, ensure_ascii=False)


@app.route("/title/check")
def title_check():
    if request.method == 'POST':
        title_input = request.form.get("title")
    else:
        title_input = request.args.get("title")
    code, sim_list = get_sim_title(title_input)
    result = {"code": code, "data": {"match_info": sim_list[0], 'title_input': title_input}, "msg": 'ok'}
    return json.dumps(result, ensure_ascii=False)


if __name__ == '__main__':
    """
       使用flask自带的传递参数threaded与processes，也可以实现异步非阻塞，但是这个原理是
       同时开启多个线程或者多个进程来接受发送的请求，每个线程或者进程还是阻塞式处理任务
       如果想使用threaded或processes参数，必须将debug设置为False才能生效，不然不起作用
       同时Windows下不支持同时开启多进程，所以在win下使用processes无效
    """
    # 在线检测
    checking_thread = threading.Thread(target=real_time_checking)
    checking_thread.start()
    print('>> 程序加载完成！')
    print('HTTP服务：0.0.0.0:5050')
    try:
        # 单线程+多协程+libevent
        http_server = WSGIServer(('0.0.0.0', 5050), app, handler_class=WebSocketHandler)
        http_server.serve_forever()
    except:
        print('HTTP服务失败/关闭')
