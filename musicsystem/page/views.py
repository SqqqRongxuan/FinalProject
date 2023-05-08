import base64
import json
import time

from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render

from . import until


def index(request):
    return render(request, 'signin.html')

def logout(request):
    logout(request)

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    with connection.cursor() as cursor:
        sql = "select  userid from tb_user where username = '{0}' and password = '{1}' limit 0,1".format(username,
                                                                                                         password)
        cursor.execute(sql)
        res = cursor.fetchall()
    if res == ():
        return HttpResponse('The user is not sign-up')
    else:
        now = int(round(time.time() * 1000))
        now02 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now / 1000))
        with connection.cursor() as cursor:
            sql = 'update tb_user set last_login = "{0}" where userid = {1}'.format(now02, res[0][0])
            cursor.execute(sql)
        data = {
            'info': 'Successful Signin',
            'userid': res[0][0]
        }
        return HttpResponse(json.dumps(data))

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')

def res(request):
    name = request.POST['name']
    username = request.POST['username']
    password = request.POST['password']
    if username != '' and password != '':
        with connection.cursor() as cursor:
            sql = "insert into tb_user( username ,name, password ) values('%s','%s','%s')" % (username, name, password)
            cursor.execute(sql)
            connection.commit()
            return HttpResponse('Successful Signup')
    else:
        return HttpResponse("Fail Signup")


def userindex(request):
    try:
        key = request.GET['key']
        data = {
            'allsong': until.seachallsong(key)
        }
        return render(request, 'userindex.html', data)
    except:
        userid = request.GET['id']
        ib = until.ItemCF(userid)
        cfre = []
        key = ib.recommend(str(userid))
        for i in key:
            if key[i] >= 2.95:
                cfre.append(until.cfre(i))

        data = {
            'allsong': until.getallsong(),
            'cfre': cfre,
            'gxre': until.gxre()

        }
        return render(request, 'userindex.html', data)


def getuserinfo(request):
    id = request.POST['data']
    id = json.loads(id)
    data = until.getuserinfo(id['userid'])
    return HttpResponse(json.dumps(data))


def bangdinguserinfo(request):
    if request.method == 'GET':
        return render(request, 'bangdinguserinfo.html')
    elif request.method == "POST":
        try:
            id = request.POST['id']
            name = request.POST['name']
            nickname = request.POST['nickname']
            password = request.POST['password']
            phone = request.POST['phone']
            add = request.POST['add']
            sex = request.POST['sex']
            art = request.FILES['art']
            artdata = base64.b64encode(art.read())
            sql = 'update tb_user set `name`="{0}", `art`="{1}" , `nickname`="{2}" , `password`="{3}" , `sex`="{4}" , `phone`="{5}" , `add`="{6}" where userid = {7}'.format(
                name, artdata, nickname, password, sex, phone, add, id)
            until.insert(sql)
            data = {
                'info': "绑定成功"
            }
            return HttpResponse(json.dumps(data))
        except:
            data = {
                'info': "绑定失败"
            }
            return HttpResponse(json.dumps(data))


def userinfoindex(request):
    if request.method == "GET":
        userid = request.GET['id']
        data = {
            'allsong': until.getsc(userid),
            'playsong': until.getplay(userid)
        }
        return render(request, 'userinfoindex.html', data)
    else:
        userid = request.POST['data']
        id = json.loads(userid)['userid']
        userinfo, usersc, userplay = until.GetAllUserInfo(id)
        data = {
            'userinfo': userinfo,
            'usersc': usersc,
            'userplay': userplay,
        }
        return HttpResponse(json.dumps(data))


def usersc(request):
    data = request.POST['data']
    data = json.loads(data)
    songid = data['songid']
    userid = data['userid']
    data = until.sc(songid, userid)
    return HttpResponse(json.dumps(data))


def userdel(request):
    data = request.POST['data']
    data = json.loads(data)
    songid = data['songid']
    userid = data['userid']
    data = until.userdel(songid, userid)
    return HttpResponse(json.dumps(data))


def userplay(request):
    data = request.POST['data']
    data = json.loads(data)
    songid = data['songid']
    userid = data['userid']
    data = until.userplay(songid, userid)
    return HttpResponse(json.dumps(data))


def userclean(request):
    data = request.POST['data']
    data = json.loads(data)
    userid = data['userid']
    data = until.userclean(userid)
    return HttpResponse(json.dumps(data))


def seach(request):
    data = request.GET['key']
    data = {
        'allsong': until.sea(data)
    }
    return render(request, 'songindex.html', data)


def songindex(request):
    key = request.GET['key']
    data = {
        'allsong': until.seachallsong(key)
    }
    return render(request, 'songindex.html', data)


def admin(request):
    num = until.numsong()
    data = until.getauther()
    data = {
        'num': num,
        'data': data,
    }
    return render(request, 'adminindex.html', data)


def gettop(request):
    data = until.gettop()
    return HttpResponse(json.dumps(data))


def getlx(request):
    data = until.getlx()
    return HttpResponse(json.dumps(data))


def getlxtop(request):
    data = until.getlxtop()
    return HttpResponse(json.dumps(data))


def adminallmusic(request):
    data = until.adminallsong()
    data = {
        'data': data
    }
    return render(request, 'adminallmusic.html', data)


def admindel(request):
    data = request.POST['data']
    songid = json.loads(data)['songid']
    until.admindel(songid)
    data = {
        'info': "删除成功"
    }
    return HttpResponse(json.dumps(data))


def adminadd(request):
    if request.method == 'GET':
        return render(request, 'adminadd.html')
    else:
        try:
            songid = request.POST['songid']
            songname = request.POST['songname']
            songauther = request.POST['songauther']
            songlx = request.POST['songlx']
            songtime = request.POST['songtime']
            songzj = request.POST['songzj']
            songimg = request.POST['songimg']
            songpl = 0
            sql = 'insert into tb_music(`songid`,`songname`,`songauther`,`songlx`,`songtime`,`songzj`,`songpl`,`songimg`) values("%s","%s","%s","%s","%s","%s","%s","%s")' % (
                songid, songname, songauther, songlx, songtime, songzj, songpl, songimg
            )
            until.insert(sql)
            data = {
                'info': '添加成功'
            }
            return HttpResponse(json.dumps(data))
        except Exception as e:
            data = {
                'info': '添加失败,歌曲已被收录'
            }
            return HttpResponse(json.dumps(data))


def adminuser(request):
    if request.method == 'GET':
        data = until.admingetuser()
        data = {
            'data': data
        }
        return render(request, 'adminuser.html', data)


def admindeluser(request):
    data = request.POST['data']
    songid = json.loads(data)['userid']
    until.admindel(songid)
    data = {
        'info': "删除成功"
    }
    return HttpResponse(json.dumps(data))


def getlink(request):
    data = request.POST['data']
    songid = json.loads(data)['songid']
    data = until.getlink(songid)
    return HttpResponse(json.dumps(data))


def concert(request):
    data = until.concert()
    data = {'data': data}
    return render(request, 'concert.html', data)


def concertinfo(request):
    id = request.GET['id']
    data = until.concertinfo(id)
    return render(request, 'concertinfo.html', data)


def adminlogin(request):
    return render(request, 'adminlogin.html')


def paihang(request):
    data = until.getpaihang()
    data = {'data': data}
    return render(request, 'paihang.html', data)


def songdata(request):
    return render(request, 'songdata.html')


def getallsongdata(request):
    data = until.getallsongdata()
    return HttpResponse(json.dumps(data))
