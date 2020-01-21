import threading
import os
import time

def func(name):
    print(name)
    time.sleep(5)
    print('finish', name)
    
threading.Thread(target=func, args=('nodaemon',)).start()
threading.Thread(target=func, args=('daemon',), daemon=True).start()
print('aaa')