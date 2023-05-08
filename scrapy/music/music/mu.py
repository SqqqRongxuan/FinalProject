import scrapy
from Crypto.Cipher import AES
import json
import pymysql
from base64 import b64encode
from music.items import MusicItem
import until

class MuSpider(scrapy.Spider):
    name = 'mu'

    def coon(self):
        con = pymysql.connect(port=3305, password='root', user='root', host="localhost", db="music")
        cur = con.cursor()
        return con, cur

    def query(self, sql):
        con, cur = self.coon()
        cur.execute(sql)
        res = cur.fetchall()
        return res

    def start_requests(self):
        e = "010001"
        f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
        g = "0CoJUm6Qyw8W8jud"
        i = "0hyFaCNAVzOIdoht"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
        }

        def get_encSecKey():
            return "4022359ea3110bcd034e0160c3b89e5e172fd0110a3cf765d9f366d9fd09840a1f4a4705ac43719fdb8bfeb44d3b92334733061ad10942131184a4dfba0ac9d2cf867b8b6236523c1ca5f44c0d2d82c1c2665a3137a9241c7373539c1aa8e5e9bb9d33dafc764b5d76c2ab34fc94df85e27a934c8a603fa713f2cf38c2b7bbae"

        def get_params(data):  # data默认是json字符串
            first = enc_params(data, g)
            second = enc_params(first, i)
            return second

        def to_16(data):
            pad = 16 - len(data) % 16
            data += chr(pad) * pad
            return data

        def enc_params(data, key):
            iv = "0102030405060708"
            data = to_16(data)
            aes = AES.new(key=key.encode('utf-8'), IV=iv.encode('utf-8'), mode=AES.MODE_CBC)
            bs = aes.encrypt(data.encode('utf-8'))
            return str(b64encode(bs), "utf-8")

        sql = 'select songid from tb_music'
        res = self.query(sql)
        idlist = []
        for a in res:
            idlist.append(a[0])

        for j in range(1, 20):
            for id in idlist:
                page_num = str(j * 20)
                a = {
                    'csrf_token': "",
                    'cursor': "-1",
                    'offset': "0",
                    'orderType': "1",
                    'pageNo': "1",
                    'pageSize': page_num,
                    'rid': "R_SO_4_" + str(id),
                    'threadId': "R_SO_4_" + str(id)}
                data = {
                    "params": get_params(json.dumps(a)),
                    "encSecKey": get_encSecKey()
                }
                url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
                songid = {}
                songid['songid'] = id
                yield scrapy.FormRequest(url=url, method='POST', callback=self.parse, headers=headers, formdata=data,
                                         cb_kwargs=songid)

    def parse(self, response, songid):
        music_item = MusicItem()
        result = json.loads(response.text)
        for hot in range(len(result['data']['hotComments'])):
            music_item['nickname'] = result['data']['hotComments'][hot]['user']['nickname']
            music_item['content'] = result['data']['hotComments'][hot]['content']
            music_item['likedCount'] = result['data']['hotComments'][hot]['likedCount']
            music_item['songid'] = songid
            yield music_item
