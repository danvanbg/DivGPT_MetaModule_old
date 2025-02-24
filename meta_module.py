# meta_module.py
import requests
import json

class MetaModule:
    def __init__(self, chatgpt_url, api_url):
        self.chatgpt_url = chatgpt_url
        self.api_url = api_url

    def collect_data(self):
        # Събира данни от външен API (например, вашата база данни или друга система)
        response = requests.get(self.api_url + "/get_new_data")
        return response.json()

    def send_to_chatgpt(self, data):
        # Изпраща събрани данни към ChatGPT
        response = requests.post(self.chatgpt_url + "/process_data", json={"data": data})
        return response.json()

    def run(self):
        # Основен процес за извличане на данни и обработка с ChatGPT
        new_data = self.collect_data()
        processed_data = self.send_to_chatgpt(new_data)
        return processed_data

# Пример на използване на модула
if __name__ == "__main__":
    chatgpt_url = "https://your-chatgpt-api-url"  # Тук поставете URL на вашето API за ChatGPT
    api_url = "https://your-api-url"  # Тук поставете URL на вашето API за съхранение на данни

    module = MetaModule(chatgpt_url, api_url)
    result = module.run()
    print(result)
