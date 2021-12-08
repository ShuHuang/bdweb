import json
import time
import requests


API_TOKEN = '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'
API_URL = 'https://api-inference.huggingface.co/models/batterydata/bert-base-doc-classifier'


def run_classifier(inputs):
    """
    return: list (length 1) of answers (dict of label and original_question)
    """

    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    def query(payload):
        data = json.dumps(payload)
        response = requests.request("POST", API_URL, headers=headers, data=data)
        print(response.content.decode("utf-8"))
        while response.status_code == 503:
            print(response)
            time.sleep(5)
            response = requests.request("POST", API_URL, headers=headers, data=data)
        return json.loads(response.content.decode("utf-8"))[0]

    inputs = inputs
    data = query({"inputs": inputs, "wait_for_model": True})
    print(data)

    label0, label1 = data[0]['score'], data[1]['score']
    if label0 > label1:
        label = "This isn't a paragraph about battery research"
    else:
        label = "This is a paragraph about battery research"
    answers = [{'original_question': inputs, 'answer': label}]
    return answers
