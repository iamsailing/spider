# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class DoubanbookPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',user='root',passwd='root',db='spider',charset='utf8')
        self.cur =self.conn.cursor()

    def process_item(self, item, spider):
        title = item.get('title', 'N/A')
        author = item.get('author', 'N/A')
        category = item.get('category', 'N/A')
        rate = item.get('rate', 'N/A')
        count = item.get('count', 'N/A')
        brief = item.get('brief', 'N/A')

        sql = "insert into doubanread(title,author,category,rate,count,brief) values (%s, %s, %s, %s, %s, %s)"
        self.cur.execute(sql,(title,author,category,rate,count,brief))
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

