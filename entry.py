import time
import random
from redis import Redis
from rq import Queue

from work import long_running_chore

q = Queue(connection=Redis())

while True:
    print("Enqueueing job!")
    result = q.enqueue(long_running_chore, random.randint(10, 20))
    time.sleep(2)
    