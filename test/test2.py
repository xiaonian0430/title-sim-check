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
from service.article_es import sync_title, get_sim_title

print('>> 同步标题...')
# sync_title()
print('>> 同步标题完毕')

if __name__ == '__main__':
    title_list = [
        '“游客在九寨沟光脚下水拍照”，网友怒了',
        '厉害了！孕妇遇车祸身亡，腹中胎儿“受力”从子宫内飞出，奇迹降生',
        '80多岁老头要离婚,老婆跪地哭着哀求不要离婚',
        '她11岁结婚，因长得太美被印在壹元人民币上，活到90岁，名字耳熟',
        '哥哥去世后,弟弟帮嫂子搬家,掀开沙发时整个人都傻眼了!',
        '北大教授夫人陈司寇96岁断食结束生命,生前留下一句话很有哲理',
        '54岁周涛近照曝光，状态看傻网友：二婚嫁富豪，曾经的“央视一姐”绝了！',
        '101岁的老夫妻打架,却看哭千万人!感动!',
        '老人进城看当“大官”儿子，趁儿媳出门，无意间发现儿子的遗像',
        '老鼠追着蛇满大街跑,仔细观察后,路人都被感动泪目了',
        '人到中年,与人关系再好,也不要透露以下3个秘密',
        '这种缝纫机价格已翻50倍!你家还有吗?',
        '陕西90岁老奶奶，生前拒绝上户口，临死前交出一张照片，揭露身份',
    ]
    for title in title_list:
        code, sim_list = get_sim_title(title)
        print(sim_list)
        break
    exit(0)
    title_list = [
        '小朋友怎样吃更健康？科学膳食，健康成长！【新时代健康科普作品征集大赛展播（20）】',
        '“游客在九寨沟光脚下水拍照”，网友怒了',
        '四部门发文遏制天价月饼，协同联动严纠不正之风',
        '早逝的人有个共同点,那就是这里先“死掉”了!',
        '拥有这些特征的人,更容易长寿',
        '养身、养心更养胃,冬季最佳养生食物大推荐',
        '称中国旗袍娃娃为“日本艺伎”，名创优品致歉!',
        '60岁房东给21岁女租客发不雅视频',
        '猫咪趁主人睡觉开闸放水淹了家',
        '三男孩跪楼道里饮料代酒桃园结义',
    ]
    for title in title_list:
        code, sim_list = get_sim_title(title)
        print(sim_list)
