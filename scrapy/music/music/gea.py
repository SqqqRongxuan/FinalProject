import time
import pyhdfs
from lxml import html
from selenium import webdriver
import requests
import until


driver = webdriver.Firefox()
# for g in ['流行', '摇滚', '民谣', '电子', '舞曲', '说唱', '轻音乐', '爵士', '乡村', 'R&B/Soul', '古典', '民族', '英伦', '金属', '蓝调', '雷鬼', '世界音乐',
#           '拉丁', 'New Age', '古风', 'Bossa Nova']:
for g in ['Popular', 'Rock', 'Folk', 'Electron', 'Dance', 'Rap', 'Light', 'Jazz', 'R&B/Soul', 'Classical', 'Nation',
     'England', 'Blues', 'Reggae','World', 'Latin', 'New Age', 'Ancient', 'Bossa Nova']:
    for i in range(0, 70, 35):
        try:
            url = 'https://music.163.com/#/discover/playlist/?order=hot&cat={0}&limit=35&offset={1}'.format(g, str(i))
            driver.get(url)
            driver.switch_to.frame("g_iframe")
            page = driver.page_source
            etree = html.etree.HTML(page)
            ul = etree.xpath('/html/body/div[3]/div/ul')
            for y in ul:
                href = y.xpath('li/div/a/@href')
            for x in href:
                url = 'https://music.163.com' + x
                driver.get(url)
                time.sleep(1)
                driver.switch_to.frame("g_iframe")
                page = driver.page_source
                etree = html.etree.HTML(page)
                SongUrl = etree.xpath(
                    '/html/body/div[3]/div[1]/div/div/div[2]/div[2]/div/div[1]/table/tbody/tr/td[2]/div/div/div/span/a/@href')
                songtime = etree.xpath(
                    '/html/body/div[3]/div[1]/div/div/div[2]/div[2]/div/div[1]/table/tbody/tr/td[3]/span/text()')
                zj = etree.xpath(
                    '/html/body/div[3]/div[1]/div/div/div[2]/div[2]/div/div[1]/table/tbody/tr/td[5]/div/a/@title')
                auther = etree.xpath(
                    '/html/body/div[3]/div[1]/div/div/div[2]/div[2]/div/div[1]/table/tbody/tr/td[4]/div/@title')
                for z in range(len(SongUrl)):
                    try:


                        songurl = 'https://music.163.com/#' + SongUrl[z]
                        driver.get(songurl)
                        time.sleep(1)
                        driver.switch_to.frame("g_iframe")
                        page = driver.page_source
                        etree = html.etree.HTML(page)
                        songimg = etree.xpath(
                            '/html/body/div[3]/div[1]/div/div/div[1]/div[1]/div[1]/div[1]/img/@data-src')
                        songpl = etree.xpath('//*[@id="cnt_comment_count"]/text()')
                        songname = etree.xpath(
                            '/html/body/div[3]/div[1]/div/div/div[1]/div[1]/div[2]/div[1]/div/em/text()')
                        sql = 'insert into tb_music(`songid`,`songtime`,`songauther`,`songzj`,`songimg`,`songpl`,`songlx`,`songname`) values ("%s","%s","%s","%s","%s","%s","%s","%s")' % (
                            SongUrl[z].split('=')[1], songtime[z], auther[z], zj[z], songimg[0], songpl[0], g, songname[0]
                        )
                        print(SongUrl[z].split('=')[1])
                        link_url = 'https://link.hhtjim.com/163/' + SongUrl[z].split('=')[1] + '.mp3'
                        musci_name = songname[0]+'.mp3'
                        info =requests.get(link_url).content
                        path = r'C:\Users\Administrator\Desktop\update\music\page\musicdata\\'+musci_name
                        with open(path,'wb+') as w:
                            w.write(info)
                            w.flush()
                            w.colse()
                        # until.insert(sql)
                    except Exception as e:
                        print(e)
                        continue
        except Exception as e:
            continue


