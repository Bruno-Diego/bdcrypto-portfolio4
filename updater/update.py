from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from updater import api


def start():
    """
    Scheduler to update the coins
    """
    scheduler = BackgroundScheduler()
    scheduler.add_job(api.update_coins, 'interval', days=1)
