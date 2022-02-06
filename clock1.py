from apscheduler.schedulers.background  import BlockingScheduler
from gsheet import export_to_gsheet
sched = BlockingScheduler()


def maina():
    """Run tick() at the interval of every ten seconds."""
   
    sched.add_job(export_to_gsheet, 'interval', minutes=6)
    try:
        sched.start()
    except (KeyboardInterrupt, SystemExit):
        pass 


maina()


