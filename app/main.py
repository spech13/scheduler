from datetime import datetime, timedelta
from scheduler import Scheduler

@Scheduler.scheduling_decorator(
    datetime.now() + timedelta(seconds=10),
    repeat=timedelta(seconds=5),
    stop=datetime.now() + timedelta(seconds=43),
)
def notification_about_exam():
    print(f"You have a exam: current time {datetime.now()}")


@Scheduler.scheduling_decorator(
    datetime.now() + timedelta(seconds=20), repeat=timedelta(seconds=10), max_retry=2
)
def notification_about_interview():
    print(f"You have a interview: current time {datetime.now()}")

@Scheduler.scheduling_decorator(datetime.now() + timedelta(seconds=5))
def law_of_universal_gravitation(m1, m2, r):
    print(f"Force of gravity: {6.67 * pow(10, -11) *  m1 * m2 / (r*r)}")

EARTH_MASS_KG = 6 * pow(10, 24)
MOON_MASS_KG = 7.3 * pow(10, 22)
DISTANCE_M = 3.844 * pow(10, 8)

tasks = (
        (notification_about_interview, ()),
        (notification_about_exam, ()),
        (law_of_universal_gravitation , (EARTH_MASS_KG, MOON_MASS_KG, DISTANCE_M)),
    )

scheduling = Scheduler()
scheduling.extend_tasks(tasks)
scheduling.delay()
