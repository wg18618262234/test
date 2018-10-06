# coding=utf-8
import websocket
import datetime, time, json,os

try:
    import thread
except ImportError:
    import _thread as thread

guanqia, wujinlianyu, lasttime, num = 0, 0, 0, 0


# 服务器返回信息打印
def on_message(ws, message):
    global guanqia, lasttime, wujinlianyu
    # print(message)
    # if (json.loads(message).get('k') and json.loads(message).get('k') != int(guanqia)):
    #     guanqia = int(guanqia) + 1
    if json.loads(message).get('lastGuaJiTime'):
        lasttime = json.loads(message).get('lastGuaJiTime')
        # print('最后挂机时间：%s' % json.loads(message).get('lastGuaJiTime'))
    if json.loads(message).get('k'):
        guanqia = json.loads(message).get('k')
        # print('当前挑战BOSS关卡是：%s' % guanqia)
        # print('服务器返回BOSS关卡是：%s' % json.loads(message).get('k'))
    if json.loads(message).get('pd') == 1080:
        wujinlianyu = json.loads(message).get('level')
        # print('服务器返回无尽炼狱已通关层数：%s' % json.loads(message).get('level'))


# 服务器异常信息打印
def on_error(ws, error):
    print(error)


# 服务器关闭信息打印
def on_close(ws):
    print("### closed ###")


# 向服务器发送参数
def on_open(ws):
    def run(*args):
        global num

        # 登陆
        ws.send('{"userName":"18618262234","passWord":"wanggang00","plat":0,"key":"","pktId":0}')
        # ws.send('{"userName":"mao8020586bu","passWord":"luozhenkun","plat":0,"key":"","pktId":0}')

        # 获取并更新最后挂机时间
        ws.send('{"levelId":0,"operate":5,"danci":0,"pktId":5}')
        print('最后挂机时间：%s' % lasttime)

        while True:
            time.sleep(0.05)
            # 获取关卡信息
            ws.send('{"pktId":2}')

            nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print('******************************************************************************************')
            print('                  第%d次挑战                   当前时间：%s' % (num, nowtime))
            print('******************************************************************************************')
            time.sleep(0.05)
            # 挑战boss
            ws.send('{"levelId":%d,"operate":2,"danci":4,"pktId":5}' % (int(guanqia)))
            print('正在挑战BOSS......       当前挑战BOSS关卡：%s' % guanqia)
            num = num + 1

            time.sleep(0.05)
            # 无尽炼狱挑战
            ws.send('{"operate":2,"pktId":244}')
            print('正在挑战无尽试炼......   当前无尽炼狱已通关：%s' % wujinlianyu)

            time.sleep(0.05)
            # # 金币副本挑战
            ws.send('{"operate":2,"fbType":1,"pktId":243}')
            print('正在挑战金币副本......')

            time.sleep(0.05)
            # # 经验副本挑战
            ws.send('{"operate":2,"fbType":2,"pktId":243}')
            print('正在挑战经验副本......')

            time.sleep(0.05)
            # # 羁绊副本挑战
            ws.send('{"operate":2,"fbType":3,"pktId":243}')
            print('正在挑战羁绊副本......')

            time.sleep(0.05)
            # # 熔炼副本挑战
            ws.send('{"operate":2,"fbType":4,"pktId":243}')
            print('正在挑战熔炼副本......')

            time.sleep(0.05)
            # # 草药副本挑战
            ws.send('{"operate":2,"fbType":5,"pktId":243}')
            print('正在挑战草药副本......')

            time.sleep(0.05)
            # # 血精副本挑战
            ws.send('{"operate":2,"fbType":6,"pktId":243}')
            print('正在挑战金币副本......')

            time.sleep(0.05)
            # 发送时间戳
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
    ws = websocket.WebSocketApp("ws://47.99.84.144:35001/",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
    time.sleep(180)
