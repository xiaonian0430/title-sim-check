# encoding: utf-8
"""
文章标题同步es
@author: xiao nian
@contact: xiaonian030@163.com
@date: 2024-01-11
"""

__copyright__ = "Copyright (c) (2022-2024) XN Inc. All Rights Reserved"
__author__ = "Xiao Nian"
__date__ = "2024-01-11 14:13:24"
__version__ = "1.0.0"

from dao.article import get_title_list
from dao.article_es import more_like_this
from tool.similar import compare
from tool.similar_bd import compare as compare_db
from dao.article_es import add_title
import time

title_id_dict = dict()


def sync_title():
    """
    同步标题
    """
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
                title_id = int(item[0])
                if title_id not in title_id_dict:
                    add_title({
                        'id': title_id,
                        'title': item[1]
                    })
                    title_id_dict[title_id] = 1
        except:
            break
    return True


def real_time_checking():
    """
    实时检测标题
    """
    while True:
        try:
            sync_title()
        except:
            pass
        time.sleep(5)


def get_sim_title(title_input):
    """
    获取相似的标题
    """
    result = more_like_this(title_input)
    sim_list = []
    try:
        num = len(result['hits']['hits'])
        if num > 0:
            for index in range(0, min(num, 1)):
                info = result['hits']['hits'][index]['_source']
                try:
                    score = compare_db(title_input, info['title'])
                except:
                    score = -1
                if score < 0:
                    score_one = round(result['hits']['hits'][index]['_score'] / 100, 4)
                    # 词向量相似度分数，通过词袋模型获取两个短文本你的
                    score_two = compare(title_input, info['title'])
                    score = round(score_two * 0.7 + score_one * 0.3, 3)
                info['score'] = score
                sim_list.append(info)
        else:
            sim_list.append({
                'score': 0,
                'title': '',
                'id': 0
            })
        code = 0
    except:
        code = 400
        sim_list.append({
            'score': 0,
            'title': '',
            'id': 0
        })
    return code, sim_list
