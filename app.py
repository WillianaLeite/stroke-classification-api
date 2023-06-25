
from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import pandas as pd
import numpy as np
import pickle
import json

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('data')
parser.add_argument('extractor_type')

class StrokeClassifier(Resource):

    def predict(self, X: np.array, type_extractor: str):
        
        with open(f'model/extratree_{type_extractor}.pkl', 'rb') as f:
            self.model = pickle.load(f)

        if type_extractor == 'percent':
            cols = [f'proba_class_{i}' for i in range(12)]
        elif type_extractor == 'pixel':
            cols = [f'pixel_{i}' for i in range(11858)]
        
        if len(X.shape) == 1: X = [X]

        df_test = pd.DataFrame(X, columns=cols)
        return self.model.predict(df_test)

    def post(self):

        args = parser.parse_args()
        extractor_type = args['extractor_type']
        data = np.array(json.loads(args['data']))
        
        return jsonify(self.predict(data, extractor_type).tolist())

api.add_resource(StrokeClassifier, '/stroke')

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=5000)