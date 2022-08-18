import os

from apscheduler.schedulers.background import BackgroundScheduler

job = BackgroundScheduler(daemon=True)

module_path = os.path.dirname(os.path.realpath(__file__))


def free_storage():
    dir = module_path + "/tmp/"
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))


job.add_job(free_storage, "interval", minutes=1)

job.start()
