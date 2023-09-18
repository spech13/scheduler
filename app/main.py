from datetime import datetime, timedelta
from scheduler import Scheduler


@Scheduler.scheduling_decorator(datetime.now() + timedelta(seconds=5))
def notification_about_train():
    print("You have a train")


@Scheduler.scheduling_decorator(datetime(2023, 9, 18, 15, 59, 0))
def notification_about_doctor():
    print("You have an appointment with a doctor though 30 minutes")


scheduling = Scheduler()
scheduling.extend_tasks((notification_about_doctor, notification_about_train))
scheduling.delay()
