import threading

from datetime import datetime, timedelta
from time import sleep


class Scheduling:
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


@Scheduling.scheduling_decorator(datetime.now() + timedelta(seconds=5))
def notification_about_train():
    print("You have a train")


@Scheduling.scheduling_decorator(datetime(2023, 9, 17, 17, 46, 0))
def notification_about_doctor():
    print("You have an appointment with a doctor though 30 minutes")


scheduling = Scheduling()
scheduling.extend_tasks((notification_about_doctor, notification_about_train))
scheduling.delay()
