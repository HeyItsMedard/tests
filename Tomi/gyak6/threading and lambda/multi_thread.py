import threading
import time

def thread_function(number):
  print("Starting thread:", number)
  time.sleep(2)
  print("Finished thread:", number)

threads = list()
print("Before thread")
for i in range(3):
  x = threading.Thread(target=thread_function, args=(i, ))
  threads.append(x)
  x.start()
print("Waiting for thread")
for index, thread in enumerate(threads):
  print("Before:", index)
  thread.join()
  print("After:", index)

print("After thread")
