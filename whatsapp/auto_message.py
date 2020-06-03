
from apscheduler.schedulers.blocking import BlockingScheduler
from Automation_whatsp import msg

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(msg, 'interval', seconds=5)

sched.start()