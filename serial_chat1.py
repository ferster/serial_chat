import serial
import threading
import time

ser = serial.Serial('/dev/ttyS0', 9600, timeout=5)
ser2 = serial.Serial('/dev/ttyS1', 9600, timeout=5)

def recv():
    while 1:
        data = ser2.read(50)
        if data != b'':
            print("[RECV "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"]"+str(data, encoding = "utf-8"))


def send():
    while 1:
        data = input()
        if (data != ''):
            ser.write(("[SEND " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "]" +data).encode())
            print("[SEND " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "]" +data)



while True:
    thread1 = threading.Thread(target=send, name='sendThread')
    thread2 = threading.Thread(target=recv, name='recvThread')
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
