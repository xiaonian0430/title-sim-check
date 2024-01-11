from config import config
from elasticsearch7 import Elasticsearch


def connect():
    return Elasticsearch(
            hosts=config.es['hosts'],
            http_auth=config.es['http_auth'],
            # 在做任何操作之前，先进行嗅探
            # sniff_on_start=True,
            # # 节点没有响应时，进行刷新，重新连接
            sniff_on_connection_fail=True,
            # # 每 60 秒刷新一次
            sniffer_timeout=60
        )


def add_title(data):
    index_name = 'article_index'
    es = connect()
    # 索引存在，先删除索引
    if not es.indices.exists(index_name):
        request_body = {
            'mappings': {
                'properties': {
                    'title': {
                        'type': 'text'
                    },
                    'id': {
                        'type': 'integer'
                    },
                }
            }
        }
        es.indices.create(index=index_name, body=request_body)

    # 增加数据
    exist = es.exists(index=index_name, id=data['id'])
    if not exist:
        es.index(index=index_name, id=data['id'], body=data)


def more_like_this(title):
    index_name = 'article_index'
    es = connect()
    body = {
        'query': {
            "more_like_this": {
                "fields": [
                    "title"
                ],
                "like": [title],
                "analyzer": "ik_max_word",  # ik_smart
                "min_doc_freq": 1,
                "min_term_freq": 1,
                "max_query_terms": 20
            }
        }
    }

    return es.search(index=index_name, body=body)
