from time import sleep

from my_fruit_shop.celery import app


@app.task(bind=True)
def send(self, user_id):
    for i in range(20):
        sleep(1)
        self.update_state(state='PROGRESS', meta={'current': i * 5, 'total': 100})
    return {'current': 100, 'total': 100}
