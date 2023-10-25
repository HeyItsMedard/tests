import threading
import time

def thread_function(number):
  print("Starting thread:", number)
  time.sleep(2)
  print("Finished thread:", number)

print("Before thread")
x = threading.Thread(target=thread_function, args=(1, ), daemon=True)
x.start()
print("Waiting for thread")
x.join()

print("After thread")
