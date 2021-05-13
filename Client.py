import socket
import time

# def get_ip():
#     url = r'http://www.trackip.net/'
#     r = requests.get(url)
#     txt = r.text
#     ip = txt[txt.find('title')+6:txt.find('/title')-1]
#     return (ip)

def main():
    print("Client started...")
    while True:
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect(("your.server.ip.here",11086))
            s.send("qwerty123456".encode("utf-8"))
            print("send data...")
            s.close()
        except:
            print("failed, retrying...")
        time.sleep(30)

if __name__ == "__main__":
    main()
