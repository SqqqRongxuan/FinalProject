from lxml import html
from selenium import webdriver

import until

driver = webdriver.Chrome("chromedriver.exe")
driver.get(
    'https://search.damai.cn/search.htm?spm=a2oeg.home.category.ditem_5.591b23e1mFqrcC&ctl=%E9%9F%B3%E4%B9%90%E4%BC%9A')
reponse = driver.page_source
data = html.etree.HTML(reponse)
div = data.xpath('/html/body/div[2]/div[2]/div[1]/div[3]/div[1]/div/div')
for item in div:
    info_url = 'https:' + item.xpath('.//div/div[1]/a/@href')[0]
    img = item.xpath('.//a/img/@data-src')[0]
    name = item.xpath('.//div/div[1]/a/text()')[0]
    add = item.xpath('.//div/div[2]/text()')[0]
    time = item.xpath('.//div/div[3]/text()')[0]
    price = item.xpath('.//div/div[5]/span/text()')[0]
    driver.get(info_url)
    reponse = driver.page_source
    data = html.etree.HTML(reponse)
    info = data.xpath('/html/body/div[2]/div/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/p//text()')
    infostr = ''
    for i in info:
        infostr += i
    sql = 'insert into tb_concert(`img`,`name`,`add`,`time`,`price`,`info`) values ("%s","%s","%s","%s","%s","%s")' % (
        img, name, add, time, price, infostr
    )
    try:
        until.insert(sql)
    except Exception as e:
        print(e)
        continue
