import requests

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_data = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json=json_data)
    
    if response.status_code == 200:
        return response.json()['emotionPredictions'][0]['emotion']
    else:
        return {"error": "Request failed with status " + str(response.status_code)}
print (emotion_detector("I am feeling very happy and joyful today"))