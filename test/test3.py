import time

from gevent import monkey

monkey.patch_all()
import gevent
from service.handle_image import download_image


def f(url):
    local_path = '../data/image'
    local_file = download_image(url, local_path)
    print(local_file)


spawn_list = []
spawn_list.append(gevent.spawn(f,
                               'http://wx.qlogo.cn/mmopen/Q3auHgzwzM7AgIP5I0HXticp8hcUufAqtEicbMhk6b92R3wjqOhjAYq2dTaGYUx9HczVDS1VDDSySwvHTbZk0AG2bByD50WarcSDeEYlDUmoQ/64'))
spawn_list.append(gevent.spawn(f,
                               'http://wx.qlogo.cn/mmopen/Q3auHgzwzM7AgIP5I0HXticp8hcUufAqtEicbMhk6b92R3wjqOhjAYq2dTaGYUx9HczVDS1VDDSySwvHTbZk0AG2bByD50WarcSDeEYlDUmoQ/64'))
spawn_list.append(gevent.spawn(f,
                               'http://wx.qlogo.cn/mmopen/Q3auHgzwzM7AgIP5I0HXticp8hcUufAqtEicbMhk6b92R3wjqOhjAYq2dTaGYUx9HczVDS1VDDSySwvHTbZk0AG2bByD50WarcSDeEYlDUmoQ/64'))
gevent.joinall(spawn_list)

exit(200)
