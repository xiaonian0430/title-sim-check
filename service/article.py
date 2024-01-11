# encoding: utf-8
"""
文章标题
@author: xiao nian
@contact: xiaonian030@163.com
@date: 2022-09-08
"""

__copyright__ = "Copyright (c) (2022-2022) XN Inc. All Rights Reserved"
__author__ = "Xiao Nian"
__date__ = "2022-09-10:14:13:24"
__version__ = "1.0.0"
from dao.article import get_title_list
import time
from gevent import pool
from tool.similar import multi_compare

title_set = set()

"""
同步标题
"""


def sync_title():
    global title_set
    last_id = 0
    page_size = 100
    while True:
        try:
            title_list = get_title_list(last_id, page_size)
            num = len(title_list)
            if num == 0:
                break
            last_id = int(title_list[num - 1][0])
            for item in title_list:
                title_set.add(item)
        except:
            break
    return True


"""
实时检测标题
"""


def real_time_checking():
    while True:
        try:
            sync_title()
        except:
            pass
        time.sleep(5)


def get_sim_title(title_input):
    try:
        my_pool_patch = pool.Pool(10)
        my_poop_data = []
        for item in title_set:
            my_poop_data.append((item[0], item[1], title_input))
        result_list = my_pool_patch.map(multi_compare, my_poop_data)
        result_list.sort(key=lambda x: x[2], reverse=True)
        sim_list = []
        sim_num = 1
        for item in result_list:
            sim_title = item[1]
            sim_id = int(item[0])
            sim_score = item[2]
            sim_list.append({
                'score': sim_score,
                'title': sim_title,
                'id': sim_id
            })
            sim_num = sim_num - 1
            if sim_num <= 0:
                break
        code = 0
    except:
        code = 400
        sim_list = []
    if len(sim_list) <= 0:
        sim_list.append({
            'score': 0,
            'title': '',
            'id': 0
        })
    return code, sim_list
