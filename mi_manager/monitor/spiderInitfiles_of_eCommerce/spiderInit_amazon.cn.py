# -*- coding: utf-8 -*-
import redis

import mi.settings as prime_settings
from monitor.mysqlHelper import MysqlHelper


def init():

    print "try insert eCommerceId......"
    try:
        db = MysqlHelper()
        sql = "insert into ECommerce(eCommerceName, eCommerceUrl) values('amazon.cn', 'https://www.amazon.cn');".encode(encoding='utf-8')
        db.insert(sql)
        print "insert eCommerceId success"
    except Exception:
        print "insert eCommerceId failed"

    print "pushing amazon:start_url......"

    try:
        r = redis.Redis(prime_settings.REDIS_HOST, prime_settings.REDIS_PORT)
        r.delete("amazon:start_urls")
        r.delete("amazon:dupefilter" + "0")
        r.delete("amazon:requests")
        r.lpush("amazon:start_urls", 'https://www.amazon.cn/%E6%95%B0%E7%A0%81%E5%BD%B1%E9%9F%B3/dp/B014KP76G6/ref=sr_1_4?s=pc&ie=UTF8&qid=1493610822&sr=1-4&keywords=fire%E5%B9%B3%E6%9D%BF&th=1')
        print "pushing amazon:start_url success"
    except Exception:
        print "pushing amazon:start_url failed"
if __name__ == '__main__':
    init()


# -*- coding: utf-8 -*-
import redis
import monitor.settings as prime_settings
from monitor.mysqlHelper import MysqlHelper


def init():
    print "try insert eCommerceId......"
    try:
        db = MysqlHelper()
        sql = "insert into ECommerce(eCommerceName, eCommerceUrl) values('amazon', 'https://www.amazon.cn');".encode(encoding='utf-8')
        db.insert(sql)
        print "insert eCommerceId success"
    except Exception:
        print "insert eCommerceId failed"

    print "pushing jd:start_url......"
    try:
        r = redis.Redis(prime_settings.REDIS_HOST, prime_settings.REDIS_PORT, db=prime_settings.FILTER_DB)
        r.delete("jd:start_urls")
        r.delete("jd:dupefilter" + "0")
        r.delete("jd:requests")
        r.lpush("jd:start_urls", 'https://www.amazon.cn')
        print "pushing jd:start_url success"
    except Exception:
        print "pushing jd:start_url failed"
if __name__ == '__main__':
    init()
