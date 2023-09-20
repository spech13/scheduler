# scheduler
Scheduler class for invoking of methods in specific time

description:
<pre>
<span style="color=blue">fields:</span>
    tasks - list tasks of type Task
methods:
    append_task - add task in tasks list
        args:
            task - target method
            args - method args
    extend_tasks - extend tasks in list tasks
        args:
            tasks - a list of tasks consisting of tuples where the first element of the tuple is the target method, and the second is a tuple of its arguments
    delay - causes tasks to run asynchronously
decorator:
    scheduling_decorator - assigns a task execution time, repetition interval, and execution stop time
        args:
            date - execution date of target method
            repeat - repeat interval
            max_retry - number of repetitions
            stop - stop date of target method
</pre>

necessary:
<pre>
installed git and python
</pre>

preparation:
<pre>
1. execute command: git clone https://github.com/spech13/scheduler.git
2. go to "shceduler/app" directory
3. execute command: python main.py
</pre>

verifying:
<pre>
1. Notification about exam will be show ten second later and repeat five second six time
2. Notification about interview will be show twenty second later and repeat ten second two time
3. The calculation of the gravitational force between the earth and the moon will be output after five seconds once
</pre>