# coding=utf-8
import websocket

try:
    import thread
except ImportError:
    import _thread as thread
import time
import json

guanqia = 0
num = 0


# 服务器返回信息打印
def on_message(ws, message):
    global guanqia
    # print(message)
    # if (json.loads(message).get('k') and json.loads(message).get('k') != int(guanqia)):
    #     guanqia = int(guanqia) + 1
    if json.loads(message).get('k'):
        guanqia = json.loads(message).get('k')
        print('当前挑战BOSS关卡是：%s' % guanqia)
        print('服务器返回BOSS关卡是：%s' % json.loads(message).get('k'))
    if json.loads(message).get('pd') == 1080:
        print('服务器返回无尽炼狱已通关层数：%s' % json.loads(message).get('level'))


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    def run(*args):
        global guanqia
        global num
        # 登陆
        ws.send('{"userName":"18618262234","passWord":"wanggang00","plat":0,"key":"","pktId":0}')
        # ws.send('{"userName":"mao8020586bu","passWord":"luozhenkun","plat":0,"key":"","pktId":0}')
        while True:
            time.sleep(0.3)
            # 获取关卡信息
            ws.send('{"pktId":2}')
            time.sleep(0.3)
            # 挑战boss
            ws.send('{"levelId":%d,"operate":2,"danci":4,"pktId":5}' % (int(guanqia)))
            print('******************************************************************************************')
            print('                                     第%d次挑战' % num)
            print('******************************************************************************************')
            num = num + 1
            time.sleep(0.3)
            # 无尽炼狱挑战
            ws.send('{"operate":2,"pktId":244}')
            # time.sleep(0.3)
            # # 草药副本挑战
            # ws.send('{"operate":2,"fbType":5,"pktId":243}')
            # time.sleep(0.3)
            # # 自动挑战下一回合
            # ws.send('{"pktId":-1}')
            # ws.send('{"levelId":890,"operate":1,"danci":1,"pktId":5}')
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
