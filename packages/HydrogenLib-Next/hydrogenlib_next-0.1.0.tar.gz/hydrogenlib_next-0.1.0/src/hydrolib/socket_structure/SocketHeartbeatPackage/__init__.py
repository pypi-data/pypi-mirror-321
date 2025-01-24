import datetime

from src.hydrolib import threading_methods
from src.hydrolib.socket_plus import SyncSocket
from src.hydrolib.SocketStructure import SocketPost


class HeartbeatPacketClient:
    def __init__(self):
        """
        自动发送心跳包
        """
        self.sock = SyncSocket()
        self.post = SocketPost(self.sock)
        self.timer = None

    def connect(self, lc_port, rc_host, rc_port):
        self.sock.bindport(lc_port)
        res = self.sock.connect(rc_host, rc_port)
        if res is False:
            raise self.sock.getlasterror() from None

    def start(self, time=15):
        def send():
            self.post.send(time=datetime.datetime.now())

        self.timer = ThreadingPlus.threading.Timer(time, send)
        self.timer.daemon = True
        self.timer.start()

    def cancel(self):
        self.timer.cancel()


class HeartbeatPacketServer:
    """
    自动接收并相应心跳包
    """

    def __init__(self):
        self.thread = None
        self.sock = SyncSocket()
        self.post = SocketPost(self.sock)
        self.timer = None
        self.timeout = 5
        self.last_packet = None

    def listen(self):
        self.sock.listen()

    def accept(self):
        self.sock.self_accept()

    def start(self):
        def wrapper():
            while True:
                packet = self.post.top()  # 读取
                # 根据协议，这个包应该是一个_Post字典，且time值是一个datatime类型
                if "time" not in packet:
                    continue
                if not isinstance(packet.top("time"), datetime.datetime | datetime.timedelta):
                    continue
                self.last_packet = packet
                self.post.send(res="OK")  # 响应

        self.thread = ThreadingPlus.run_new_daemon_thread(wrapper)

    def check(self):
        time = datetime.datetime.now() - self.last_packet.top('time')
        seconds = time.total_seconds()
        if seconds > self.timeout:
            return False
        else:
            return True
