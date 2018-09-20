# coding=gbk
import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        ws.send('{"userName":"18618262234","passWord":"wanggang00","plat":0,"key":"","pktId":0}')
        # ws.send('{"userName":"mao8020586bu","passWord":"luozhenkun","plat":0,"key":"","pktId":0}')
        ws.send('{"pktId":2}')
        for i in range(1000):
            time.sleep(1)
            ws.send('{"levelId":%d,"operate":2,"danci":4,"pktId":5}'%(int(guanqia)))
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    guanqia = input('输入关卡数：')
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://47.99.84.144:35001/",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    if(ws.run_forever()):
        print(guanqia)