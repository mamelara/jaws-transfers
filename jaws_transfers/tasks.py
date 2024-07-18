import subprocess
from jaws_transfers.celery_app import app

@app.task(bind=True)
def rsync_transfer(self, source, destination):
    cmd = ["rsync", "-avz", source, destination]
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        raise Exception(f'rsync error: {stderr.decode()}')

    return stdout.decode()