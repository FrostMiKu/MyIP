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
            s.connect(("cloud.frostmiku.com",11086))
            s.send(bytes("qwerty123456","utf-8"))
            print("send data...")
            s.close()
        except:
            print("failed, retrying...")
        time.sleep(30)

if __name__ == "__main__":
    main()
