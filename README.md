# scheduler
Scheduler class for invoking of methods in specific day

necessary: installed git and python

preparation:
1. execute command: git clone https://github.com/spech13/scheduler.git
2. go to "shceduler/app" directory
3. execute command: python main.py

verifying:
1. You will see two messages: "You have a train" and "You have an appointment with a doctor though 30 minutes"
2. "You have a train" message will be show five seconds later
3. "You have an appointment with a doctor though 30 minutes" message will be show in that momemt, which specified in decorator params
4. If you saw "You late" message, you need change date in decorator params of method "notification_about_doctor" to more after than now