import pymysql
from config import config


def connect():
    return pymysql.connect(
        host=config.mysql_ad['host'],
        port=config.mysql_ad['port'],
        user=config.mysql_ad['user'],
        passwd=config.mysql_ad['passwd'],
        db=config.mysql_ad['dbname'],
        charset=config.mysql_ad['charset'])


def get_title_list(last_id=0, page_size=10):
    start = 0
    conn = connect()
    # 创建游标
    cursor = conn.cursor()
    # 执行SQL
    sql = 'select id,title from cr_article where id>' + str(last_id) + ' ORDER BY id ASC LIMIT ' + str(start) + ',' + str(page_size)
    cursor.execute(sql)
    # 获取全部数据
    data = cursor.fetchall()
    # 关闭数据库连接
    conn.close()
    return data

