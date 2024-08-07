import os

broker_url = os.environ.get("CELERY_BROKER_URL", "pyamqp://guest@localhost//")
imports = ("jaws_transfers.tasks",)
result_backend = os.environ.get("CELERY_RESULT_BACKEND", "db+sqlite:///results.db")