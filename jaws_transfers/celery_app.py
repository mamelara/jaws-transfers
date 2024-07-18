from celery import Celery
import jaws_transfers.celeryconfig

app = Celery('jaws_transfers')
app.config_from_object(jaws_transfers.celeryconfig)

if __name__ == '__main__':
    app.start()
