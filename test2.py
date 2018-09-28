# coding=utf-8
import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time
import json

def on_message(ws, message):
    global guanqia
    print('__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________')
    print(message)
    if (json.loads(message).get('k') and json.loads(message).get('k')!=int(guanqia)):
        guanqia = int(guanqia) + 1
    print('当前挑战BOSS关卡是：%s'%guanqia)
    if json.loads(message).get('k'):
        print('服务器返回BOSS关卡是：%s' % json.loads(message).get('k'))
    if json.loads(message).get('pd')==1080:
        print('服务器返回无尽炼狱已通关层数：%s'%json.loads(message).get('level'))
    print('__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________')

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        global guanqia
        ws.send('{"userName":"18618262234","passWord":"wanggang00","plat":0,"key":"","pktId":0}')
        # ws.send('{"userName":"mao8020586bu","passWord":"luozhenkun","plat":0,"key":"","pktId":0}')
        while True:
            time.sleep(0.3)
            # 获取关卡信息
            ws.send('{"pktId":2}')
            time.sleep(0.3)
            # 挑战boss
            ws.send('{"levelId":%d,"operate":2,"danci":4,"pktId":5}'%(int(guanqia)))
            time.sleep(0.3)
            # 无尽炼狱挑战
            ws.send('{"operate":2,"pktId":244}')
            time.sleep(0.3)
            # 草药副本挑战
            ws.send('{"operate":2,"fbType":5,"pktId":243}')
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())


while True:
    # guanqia = input('输入关卡数：')
    guanqia = 895
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://47.99.84.144:35001/",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()