import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        url =  'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
        response = requests.get(url)
        return response.content


    def load_json(self):
        response_content = self.get_response_body()
        try:
            data = json.loads(response_content)
            return data
        except json.JSONDecodeError:
            # Handle JSON decoding error, e.g., by returning None or raising an exception
            return None