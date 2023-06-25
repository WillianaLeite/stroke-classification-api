import requests
import json

cols = ['proba_class_0', 'proba_class_1', 'proba_class_2', 'proba_class_3',
        'proba_class_4', 'proba_class_5', 'proba_class_6', 'proba_class_7',
        'proba_class_8', 'proba_class_9', 'proba_class_10', 'proba_class_11']
sample_test = [0.020161, 0.326613, 0.531754, 0.073085, 0.046371, 0.002016, 0.034945, 0.225959, 0.555176, 0.145822, 0.038098, 0.0]
payload = {'extractor_type': 'percent', 'data': json.dumps(sample_test)}
y_predict = requests.post('http://127.0.0.1:5000/stroke', json=payload, headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
print(y_predict)