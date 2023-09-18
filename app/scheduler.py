import threading
from datetime import datetime
from time import sleep


class Scheduler:
    def __init__(self, tasks=[]):
        self.tasks = tasks

    def append_task(self, task):
        self.tasks.append(task)

    def extend_tasks(self, tasks):
        self.tasks.extend(tasks)

    def delay(self):
        for task in self.tasks:
            threading.Thread(target=task).start()

    @staticmethod
    def scheduling_decorator(date):
        def wrapper(func):
            def wrapp(*args, **kwargs):
                now = datetime.now()

                if now <= date:
                    sleep((date - now).total_seconds())
                else:
                    raise ValueError("You late")

                return func(*args, **kwargs)

            return wrapp

        return wrapper
