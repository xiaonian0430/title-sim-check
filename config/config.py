# encoding: utf-8
"""
配置文件
@author: xiao nian
@contact: xiaonian030@163.com
@date: 2022-09-08
"""

__copyright__ = "Copyright (c) (2022-2024) XN Inc. All Rights Reserved"
__author__ = "Xiao Nian"
__date__ = "2022-09-10:14:13:24"
__version__ = "1.0.0"

mysql_ad = {
    'host': 'rdsrqcirvo6nz5pf0n9uo.mysql.rds.aliyuncs.com',
    'port': 3306,
    'user': 'elifesys_n2018',
    'passwd': 'eysLn#nB8m',
    'dbname': 'advertising',
    'charset': 'utf8mb4',
}

es = {
    'hosts': ['172.16.141.197:9200'],
    'http_auth': ("elastic", 'aa5626188')
}


