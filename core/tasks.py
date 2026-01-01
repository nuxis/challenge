from celery import shared_task
import json
import requests


@shared_task
def web_post_json(url, payload, timeout=10):
    r = requests.post(
        url,
        data=json.dumps(payload),
        headers={"Content-Type": "application/json"},
        timeout=timeout,
    )
    return r.status_code
