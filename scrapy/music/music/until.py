import pyhdfs
import pymysql


def coon():
    con = pymysql.connect(port=3306, password='root', user='root', host="localhost", db="music")
    cur = con.cursor()
    return con, cur


def close():
    con, cur = coon()
    cur.close()
    con.close()


def insert(sql):
    con, cur = coon()
    cur.execute(sql)
    con.commit()
    close()


def query(sql):
    con, cur = coon()
    cur.execute(sql)
    res = cur.fetchall()
    close()
    return res


def updata():
    sql = 'select * from tb_con'
    res = query(sql)

    for i in res:
        info = str(i[0]) + str(i[1]) + str(i[2]) + str(i[3])
        with open('info.txt', 'a', encoding='utf-8') as w:
            w.writelines(info)
    fs = pyhdfs.HdfsClient(hosts="192.168.12.101:50070", user_name="user")
    print(fs.listdir('/'))
    fs.copy_from_local(u"info.txt", u"/data/hdfs_data/info.txt")
    print("file upload finish")


if __name__ == '__main__':
    updata()
