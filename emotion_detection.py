import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json=input_json)

    if response.status_code == 200:
        return response.json()["text"]
    else:
        print(f"Error: {response.status_code}\n{response.content}")

text_to_analyze = "I love this new technology."
result = emotion_detector(text_to_analyze)
print(result)
