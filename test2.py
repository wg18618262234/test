# coding=utf-8
import websocket
import datetime, time, json, os

try:
    import thread
except ImportError:
    import _thread as thread

guanqia, wujinlianyu, lasttime, num, jjjifen = 0, 0, 0, 0, 0
roleid = []
rolename = []
rolezhanli = []
jinbishop = []


# 服务器返回信息打印
def on_message(ws, message):
    global guanqia, lasttime, wujinlianyu, roleid, jjjifen, jinbishop
    # print(message)
    # if (json.loads(message).get('k') and json.loads(message).get('k') != int(guanqia)):
    #     guanqia = int(guanqia) + 1

    # 获取最后挂机时间
    if json.loads(message).get('lastGuaJiTime'):
        lasttime = json.loads(message).get('lastGuaJiTime')
        # print('最后挂机时间：%s' % json.loads(message).get('lastGuaJiTime'))

    # 获取当前BOSS关卡
    if json.loads(message).get('k'):
        guanqia = json.loads(message).get('k')
        # print('当前挑战BOSS关卡是：%s' % guanqia)
        # print('服务器返回BOSS关卡是：%s' % json.loads(message).get('k'))

    # 获取无尽试炼已通关层数
    if json.loads(message).get('pd') == 1080:
        wujinlianyu = json.loads(message).get('level')
        # print('服务器返回无尽炼狱已通关层数：%s' % json.loads(message).get('level'))

    # 获取竞技积分
    if json.loads(message).get('jjJifen'):
        jjjifen = json.loads(message).get('jjJifen')

    # 获取金币商城信息
    # print(json.loads(message).get('jinbiShop'))
    if json.loads(message).get('jinbiShop'):
        jinbishop = json.loads(message).get('jinbiShop')

    # 获取竞技场信息
    if json.loads(message).get('roleList'):
        jjcinfo = json.loads(message).get('roleList')
        for i in range(5):
            # print(jjcinfo[i])
            id = jjcinfo[i].get('roleId')
            idzhanli = jjcinfo[i].get('zhanli')
            idname = jjcinfo[i].get('roleName')
            # print(zhanli, idzhanli)
            if int(zhanli) - int(idzhanli) >= 50000 and not list.count(roleid, id):
                roleid.append(id)
                rolename.append(idname)
                rolezhanli.append(idzhanli)


# 服务器异常信息打印
def on_error(ws, error):
    print(error)


# 服务器关闭信息打印
def on_close(ws):
    print("### closed ###")


# 向服务器发送参数
def on_open(ws):
    def run(*args):
        global num, roleid, rolename, rolezhanli

        # 登陆
        ws.send('{"userName":"18618262234","passWord":"wanggang00","plat":0,"key":"","pktId":0}')
        # ws.send('{"userName":"mao8020586bu","passWord":"luozhenkun","plat":0,"key":"","pktId":0}')

        # 获取并更新最后挂机时间
        ws.send('{"levelId":0,"operate":5,"danci":0,"pktId":5}')

        while True:
            print('最后挂机时间：%s' % lasttime)

            # 获取关卡信息
            time.sleep(0.05)
            ws.send('{"pktId":2}')

            # 获取竞技场信息
            time.sleep(0.05)
            ws.send('{"operate":4,"roleId":"","pktId":7}')

            # 获取商城信息
            time.sleep(0.05)
            ws.send('{"operate":0,"id":0,"num":0,"pktId":32}')

            nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print('******************************************************************************************')
            print('                  第%d次挑战                   当前时间：%s' % (num, nowtime))
            print('******************************************************************************************')

            # 挑战boss
            time.sleep(0.05)
            ws.send('{"levelId":%d,"operate":2,"danci":4,"pktId":5}' % (int(guanqia)))
            print('正在挑战BOSS......       当前挑战BOSS关卡：%s' % guanqia)
            num = num + 1

            # 无尽炼狱挑战
            time.sleep(0.05)
            ws.send('{"operate":2,"pktId":244}')
            print('正在挑战无尽试炼......   当前无尽炼狱已通关：%s' % wujinlianyu)

            # 挑战竞技场
            time.sleep(0.05)
            # print(roleid)
            for i in range(len(roleid)):
                time.sleep(0.05)
                ws.send('{"operate":2,"roleId":"%s","pktId":7}' % roleid[i])
            print('正在挑战竞技场......     当前竞技积分是：%s     当前自身战力：%s     挑战名单：%s 战力：%s' % (
                jjjifen, zhanli, rolename, rolezhanli))
            roleid = []
            rolename = []
            rolezhanli = []

            # 金币商店购买
            time.sleep(0.05)
            for i in range(len(jinbishop)):
                ws.send('{"operate":1,"id":%s,"num":1,"pktId":32}' % jinbishop[i])
            print('正在购买金币商城全部商品......')

            # 金币副本挑战
            time.sleep(0.05)
            ws.send('{"operate":2,"fbType":1,"pktId":243}')
            print('正在挑战金币副本......')

            # 经验副本挑战
            time.sleep(0.05)
            ws.send('{"operate":2,"fbType":2,"pktId":243}')
            print('正在挑战经验副本......')

            # 羁绊副本挑战
            time.sleep(0.05)
            ws.send('{"operate":2,"fbType":3,"pktId":243}')
            print('正在挑战羁绊副本......')

            # 熔炼副本挑战
            time.sleep(0.05)
            ws.send('{"operate":2,"fbType":4,"pktId":243}')
            print('正在挑战熔炼副本......')

            # 草药副本挑战
            time.sleep(0.05)
            ws.send('{"operate":2,"fbType":5,"pktId":243}')
            print('正在挑战草药副本......')

            # 血精副本挑战
            time.sleep(0.05)
            ws.send('{"operate":2,"fbType":6,"pktId":243}')
            print('正在挑战血精副本......')

            # 发送时间戳
            time.sleep(0.05)
            nowtimes = str(time.time()).replace('.', '')[:13]
            print('发送时间戳：%s' % nowtimes)
            ws.send('{"nowTime":%s,"pktId":249}' % nowtimes)

            # 战斗三回合
            for i in range(3):
                time.sleep(0.05)
                ws.send('{"levelId":%d,"operate":1,"danci":1,"pktId":5}' % guanqia)
                time.sleep(0.05)
                ws.send('{"pktId":-1}')

            os.system('cls')
        time.sleep(1)
        ws.close()
        print("thread terminating...")

    thread.start_new_thread(run, ())


while True:
    # guanqia = input('输入关卡数：')
    # guanqia = 950
    # websocket.enableTrace(True)
    zhanli = input('请输入当前总战斗力：')
    # zhanli = 380269
    ws = websocket.WebSocketApp("ws://47.99.84.144:35001/",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
    time.sleep(180)
