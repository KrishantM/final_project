import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json=input_json)

    if response.status_code == 200:
        result_dict = response.json()

        emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
        scores = {emotion: result_dict[emotion]['score'] for emotion in emotions}
        dominant_emotion = max(scores, key=scores.get)
        scores['dominant_emotion'] = dominant_emotion

        return scores
    else:
        print(f"Error: {response.status_code}\n{response.content}")

text_to_analyze = "I am so happy I am doing this."
result = emotion_detector(text_to_analyze)
print(result)
