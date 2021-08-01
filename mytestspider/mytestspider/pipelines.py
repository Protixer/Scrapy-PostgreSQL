
from itemadapter import ItemAdapter
import psycopg2 
from scrapy.exceptions import DropItem

class TutorialPipeline(object):

    def open_spider(self, spider):
        hostname = 'localhost'
        username = 'postgres'
        password = '****' # your password
        database = '****' # your name of data-base
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cur.execute("insert into public.items(title,body,url) values(%s,%s,%s)",(item['title'],item['body'],item['url']))
        self.connection.commit()
        return item