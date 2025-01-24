import random
import socket
import select

import threading
import time
import socks
from loguru import logger

from and_tools import Pack, UnPack

from .utils.sso_server import get_sso_list

clients = []
client_info = {}
lock = threading.Lock()

ip_address = ''
ip_list = {}


def repackage(data, client):
    """重组包体"""
    global client_info

    with lock:
        if client in client_info and not client._closed:
            client_info[client]['data'] = client_info[client]['data'] + data
        else:
            print(f"Socket {client} 已关闭或不存在")
            return

    pack_ = UnPack(client_info[client]['data'])
    while True:
        if pack_.get_len() <= 4:
            """小于4个字节直接跳出"""
            break
        _len = pack_.get_int()

        if _len <= pack_.get_len() + 4:
            _bin = pack_.get_bin(_len - 4)
            _func = client_info[client]['func']
            _func(_bin)
            with lock:
                if client in client_info:
                    # 安全地访问字典
                    client_info[client]['data'] = pack_.get_all()
                else:
                    logger.error(f"尝试在已关闭的套接字中写入数据: {client}")

        else:
            pack = Pack()
            pack.add_int(_len)
            pack.add_bin(pack_.get_all())
            pack_ = UnPack(pack.get_bytes())
            break


def disconnect_client(client):
    global clients, client_info, lock

    with lock:
        if client in clients:
            clients.remove(client)
            client_info.pop(client, None)
            client.close()

    return {'clients': len(clients), 'client_info': len(client_info)}


def receive_data_all():
    """在一个独立的线程中,接收并处理全部连接的数据"""
    global clients, client_info, lock

    while True:
        time.sleep(0.1)
        with lock:
            if len(clients) == 0:
                continue
            # 由于select可能会修改列表，所以使用clients[:]创建一个副本进行迭代
            readable, _, _ = select.select(clients[:], [], [], 0)

        for client in readable:
            try:
                data = client.recv(1024)
                if data:
                    repackage(data, client)
                else:
                    disconnect_client(client)
            except ConnectionResetError as e:
                logger.error(f"连接重置错误: {e}")
                disconnect_client(client)
            except OSError as e:
                if e.errno == 9:  # Bad file descriptor
                    logger.error(f"尝试操作已关闭的套接字: {e}")
                else:
                    logger.error(f"OS错误: {e}")
                disconnect_client(client)

            # if not data:
            #     disconnect_client(client, clients, client_info)
            #     log.info('断开连接')
            # else:
            #     # log.info(f"从客户端收到的数据: {data.hex()}")
            #     repackage(data, client)


def start_client(_func=None, proxy=None):
    global ip_list

    if proxy is None:
        proxy = []
    if ip_list:
        random_item = random.choice(ip_list)
        host = random_item['1']
        port = random_item['2']
    else:
        # 没初始化ip列表前用这个快速连接
        ip_list = get_sso_list()
        random_item = random.choice(ip_list)
        host = random_item['1']
        port = random_item['2']

    client = socks.socksocket()

    if len(proxy) >= 2:
        # 对于需要设置代理的客户端，创建一个配置了代理的socket对象

        if len(proxy) == 2:
            client.set_proxy(socks.SOCKS5, proxy[0], proxy[1])
        else:
            client.set_proxy(socks.SOCKS5, proxy[0], int(proxy[1]), username=proxy[2], password=proxy[3])

    try:
        client.connect((host, port))
    except socket.error as e:
        logger.info(f"连接到 {host}:{port} 失败，错误信息: {e}")
        return None

    with lock:
        client_info[client] = {'data': b'', 'func': _func}
        clients.append(client)
    return client


def get_ip_list():
    time.sleep(1)  # 超过一秒再去请求,防止测试时请求
    global ip_list
    ip_list = get_sso_list()
    # print(ip_list)


def start_tcp_service():
    """启动TCP服务"""
    threading.Thread(target=receive_data_all, daemon=True).start()

    # threading.Thread(target=get_ip_list, daemon=True).start()
    logger.info('启动接收线程')


start_tcp_service()

if __name__ == "__main__":
    ip_list = get_sso_list()
    print(ip_list)
    pass
