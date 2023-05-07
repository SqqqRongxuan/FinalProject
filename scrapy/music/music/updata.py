import pyhdfs
import pymysql


def coon():
    con = pymysql.connect(host='localhost', user='root', port=3306, password='root', db='music')
    cur = con.cursor()
    return con, cur


def close():
    con, cur = coon()
    cur.close()
    con.close()


def query(sql):
    con, cur = coon()
    cur.execute(sql)
    res = cur.fetchall()
    close()
    return res


def insert(sql):
    con, cur = coon()
    cur.execute(sql)
    con.commit()
    close()


sql = 'select * from tb_music'
res = query(sql)
for i in res:
    with open('data.txt', 'a+') as e:
        e.write(str(i[0]))

fs = pyhdfs.HdfsClient(hosts="192.168.12.101:50070", user_name="user")
fs.copy_from_local(u"data.txt", u"/data/hdfs_data/_data.txt")