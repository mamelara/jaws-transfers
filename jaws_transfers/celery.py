from celery import Celery

app = Celery('jaws_transfers',
             broker='pyamqp://guest@localhost//',
             backend='redis://localhost:6379/0',
             include=['jaws_transfers.tasks'])

print("Celery includes:", app.conf['imports'])

if __name__ == '__main__':
    app.start()
