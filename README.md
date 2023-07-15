# Stroke Classification API

## Introduction
Stroke classification in the context of this project refers to the problem of determining whether a CT scan has ischemic stroke, hemorrhagic stroke, or no stroke. Like any traditional image classification approach, we first extract features from the input images and then use some pattern classifier to determine the class of the input image.

In Leite et al. (2022) [1], an approach was proposed that achieved 99.9% accuracy for stroke classification. The approach consisted of using the extractor called Mixture Gaussian Analysis of Brain Tissue Density (MGABTD), and the Extra Tree classifier for pattern classification.

This API contains the service that makes prediction of the class of a set of MGABTD features extracted from a DICOM image. To extract MGABTD features from an image follow the library installation guide [brain-radiodensity-feature-extractor](https://github.com/WillianaLeite/brain-radiodensity-feature-extractor#installation). 

The output of this API is numerical and represents the 3 classes:
- **0**: no stroke
- **1**: ischemic stroke
- **2**: hemorrhagic stroke

## API Endpoints
| HTTP Verbs | Endpoints | Action |
| --- | --- | --- |
| POST | /stroke | To predict the class of a set of MGABTD features |


## Usage

Example preview for just one image:
```
import requests
import json
from brain_feature_extractor import BrainFeatureExtractorGMM

# Instancing the MGABTD-pixel extractor
extractor = BrainFeatureExtractorGMM(percentage=0.3, pixel_level_feature=True)

# Extracting features from the image
features = extractor.extract_features(path='sample/image157_isquemico.dcm', verbose=True)

# Send features to stroke classifier API
payload = {'extractor_type': 'pixel', 'data': json.dumps(features)}
endpoint_prod = 'http://54.204.130.82:8000/stroke'
endpoint_dev = 'http://127.0.0.1:8000/stroke'
y_predict = requests.post(endpoint_prod, json=payload, headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
print(y_predict)
```
The prediction can be done for a single image or for a set of images. If it is done for a set of images the input format must be a list of lists ```('data': json.dumps([features_first_image, features_second_image]))```. 

You can also test an API using some test tool, below is an example using Insomnia.
![insomnia-example](https://github.com/WillianaLeite/stroke-classification-api/assets/39284228/f3458333-fd34-44bf-80b2-bdcd881adf91)


## Installation Guide 

### Run without docker
You need to have Python 3 installed.

```pip3 install -r requirements.txt```

```python3 app.py ```

### Run with Docker

You need to have docker installed on your machine, if you don't already, you can follow the [installation guide](https://docs.docker.com/engine/install/).

``` docker pull willianaleite/stroke_classification:latest ```

``` docker run -p 8000:8000 willianaleite/stroke_classification:latest ```


## References

1. W. L. S. Leite, R. M. Sarmento and C. M. J. M. Dourado Junior, "Feature extraction with mixture gaussian for stroke classification," 2022 35th SIBGRAPI Conference on Graphics, Patterns and Images (SIBGRAPI), Natal, Brazil, 2022, pp. 91-96, doi: 10.1109/SIBGRAPI55357.2022.9991801.
