import threading
import time

THREADS_LIMIT = 5
CONNECTIONS_LIMIT = 2

connection_counter = 0;
semaphore = threading.BoundedSemaphore(CONNECTIONS_LIMIT)

def do_some_job():
    global connection_counter
    semaphore.acquire()
    connection_counter += 1
    print('Connection #{} started a job...'.format(connection_counter))
    assert connection_counter <= CONNECTIONS_LIMIT, 'Connection pool limit exceeded!'
    time.sleep(1)
    connection_counter -= 1
    print('Job completed!')
    semaphore.release()
    
thread_pool = []

for i in range(THREADS_LIMIT):
    thread_pool.append(threading.Thread(target=do_some_job))
    
for thread in thread_pool:
    thread.start()
    
for thread in thread_pool:
    thread.join()
    
