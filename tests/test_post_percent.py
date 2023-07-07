import requests
import json
from brain_feature_extractor import BrainFeatureExtractorGMM

# Instancing the MGABTD-percent extractor
extractor = BrainFeatureExtractorGMM(percentage=0.3, pixel_level_feature=False)

# Extracting features from the image
features = extractor.extract_features(path='sample/image157_isquemico.dcm', verbose=True)
del features[6]
del features[-1]

# Send features to stroke classifier API
payload = {'extractor_type': 'percent', 'data': json.dumps(features)}
endpoint_prod = 'http://54.204.130.82:8000/stroke'
endpoint_dev = 'http://127.0.0.1:8000/stroke'

y_predict = requests.post(endpoint_prod, json=payload, headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
print(y_predict)