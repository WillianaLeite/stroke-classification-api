import requests
import json
from brain_feature_extractor import BrainFeatureExtractorGMM

# Instancing the MGABTD-pixel extractor
extractor = BrainFeatureExtractorGMM(percentage=0.3, pixel_level_feature=True)

# Extracting features from the image
features = extractor.extract_features(path='sample/image157_isquemico.dcm', verbose=True)

# Send features to stroke classifier API
payload = {'extractor_type': 'pixel', 'data': json.dumps(features)}
y_predict = requests.post('http://127.0.0.1:8000/stroke', json=payload, headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
print(y_predict)