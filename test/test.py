# encoding: utf-8
"""
测试用例
@author: xiao nian
@contact: xiaonian030@163.com
@date: 2022-09-08
"""

__copyright__ = "Copyright (c) (2022-2022) QF Inc. All Rights Reserved"
__author__ = "Xiao Nian"
__date__ = "2022-09-10:14:13:24"
__version__ = "1.0.0"
from service.article import get_sim_title
from service.article import title_set
from service.article import sync_title

print('>> 同步标题...')
sync_title()
print('>> 同步标题完毕')

if __name__ == '__main__':
    title_input = '5岁儿子被拐卖39年后找到，亲生父母却拒绝儿子留在身边'
    code, sim_list = get_sim_title(title_input)
    print(code, sim_list)
