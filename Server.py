import socket
import threading

ip = 'Unknow...'

def web():
    global ip 
    print("Web Thread Start...")
    http_header = "HTTP/1.1 200 OK\r\nConnection: close\r\nContent-Type: text/html\r\n\r\n"
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('0.0.0.0',11085))
    s.listen(5)
    while True:
        conn,addr = s.accept()
        request_data = conn.recv(1024)
        res = http_header + "<html><head><title>My IP</title></head><body><h1>"+ip+"</h1></body></html>"
        conn.send(res.encode("utf-8"))
        conn.close()


def main():
    global ip 

    t = threading.Thread(target=web)
    t.setDaemon(True)
    t.start()

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('0.0.0.0',11086))
    s.listen(1)
    while True:
        conn,addr = s.accept()
        request_data = conn.recv(1024)
        # print(request_data)
        if request_data == b'qwerty123456': # app key
            ip = addr[0]
            print("ip updated >> "+ ip)
        conn.close()


if __name__ == "__main__":
    main()
