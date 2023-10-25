import time
import threading

class Database:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self):
        with self._lock:
          print('Before increment')
          local_copy = self.value
          local_copy += 1
          time.sleep(0.1)
          self.value = local_copy
          print('After increment')

db = Database()
threads = list()
print("Value before threads:", db.value)
for i in range(10):
    x = threading.Thread(target=db.update)
    threads.append(x)
    x.start()
for thread in threads:
    thread.join()

print('Value after threads:', db.value)
