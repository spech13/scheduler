import threading
from datetime import datetime, timedelta
from time import sleep


class Scheduler:
    class Task:
        def __init__(self, task, args):
            self.task = task
            self.args = args

    def __init__(self):
        self.tasks = []

    def append_task(self, task, args):
        self.tasks.append(self.Task(task, args))

    def extend_tasks(self, task_list):
        self.tasks.extend(self.Task(task[0], task[1]) for task in task_list)

    def delay(self):
        for task in self.tasks:
            threading.Thread(target=task.task, args=task.args).start()

    @staticmethod
    def scheduling_decorator(date, repeat=None, max_retry=None, stop=None):
        now = datetime.now()

        if type(date) is not datetime:
            raise ValueError("parametr date must be datetime")

        if repeat and type(repeat) is not timedelta:
            raise ValueError("parametr repeat must be timedelta")

        if stop and type(stop) is not datetime:
            raise ValueError("parametr stop must be datetime")

        if max_retry and type(max_retry) is not int:
            raise ValueError("parametr max_retry must be int")

        if stop and stop < date:
            raise ValueError("parametr stop must be after date")

        def wrapper(func):
            def wrapp(*args, **kwargs):
                if now > date:
                    raise ValueError(f"You late for {date}")

                sleep((date - now).total_seconds())

                if repeat:
                    count_retry = 0
                    while True:
                        func(*args, **kwargs)
                        count_retry += 1
                        sleep(repeat.total_seconds())

                        if max_retry and max_retry == count_retry:
                            break

                        if stop and datetime.now() + repeat > stop:
                            break
                else:
                    func(*args, **kwargs)

            return wrapp

        return wrapper
