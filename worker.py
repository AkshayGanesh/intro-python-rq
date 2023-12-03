#!/usr/bin/env python
from redis import Redis
from rq import Worker

# Preload libraries
from work import long_running_chore
# Provide the worker with the list of queues (str) to listen to.
w = Worker(["default"], connection=Redis())
w.work()
