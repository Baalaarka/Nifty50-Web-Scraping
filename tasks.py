from celery import Celery
# from celery.schedules import crontab
from scrap import scrap_data
from datetime import timedelta


app = Celery('tasks', broker='redis://139.59.31.78')

app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'scheduled_scraping_task': {
        'task': 'tasks.scrap_nifty',
        'schedule': timedelta(seconds=300),
        'args': (),
    },
}


@app.task
def scrap_nifty():
    scrap_data()
