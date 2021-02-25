# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class WebsitePipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("data.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute(""" DROP TABLE IF EXISTS data_tb  """)
        self.curr.execute(""" create table data_tb(
        title text,
        author text,
        desc text)""")

    def process_item(self, item, spider):
        self.store_db(item)
        print('pipelineeeeeeeeeee'+item['title'])
        return item

    def store_db(self, item):
        self.curr.execute(""" insert into data_tb values(?,?,?)""",(
            item['title'],
            item['author'],
            item['desc']
        ))
        self.conn.commit()