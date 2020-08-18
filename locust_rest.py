import json
from locust import task, between
from locust.contrib.fasthttp import FastHttpUser

from servers.common import generate_random_text


class ApiUser(FastHttpUser):
    wait_time = between(0.9, 1.1)

    @task
    def get_predictions(self):
        data = {"text": generate_random_text()}
        json_data = json.dumps(data)
        self.client.post(url="/predict", data=json_data)
