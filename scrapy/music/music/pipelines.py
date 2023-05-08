# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql


class MusicPipeline:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='music',
                                    charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = "INSERT INTO tb_con(songid,nickname,content,likecont) VALUES ('%s','%s','%s','%s')" % (
            item['songid'], item['nickname'], item['content'], item['likedCount'])
        self.cursor.execute(insert_sql)
        self.conn.commit()
