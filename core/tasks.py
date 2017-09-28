from celery import shared_task
import json
import requests

@shared_task
def web_post_json(url, payload):
    r = requests.post(
        url,
        data=json.dumps(payload),
        headers={'Content-Type': 'application/json'}
    )
    return r.status_code
