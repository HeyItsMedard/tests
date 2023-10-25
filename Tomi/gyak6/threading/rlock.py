import threading

l = threading.RLock()
print('before aquire')
l.acquire()
print('before second aquire')
l.acquire()
print('locked twice')

l.release()
l.release()
