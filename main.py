import pickle
from flask import Flask
from flask_restful import Resource, Api, reqparse
import numpy as np
from pt_to_mks import points_to_marks

app = Flask(__name__)
api = Api(app)

model = pickle.load(open('model/model.pkl', 'rb'))

class PerformancePrediction(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('Calculus And Linear Algebra')
        parser.add_argument('Engineering Physics')
        parser.add_argument('Basic Electrical Engineering')
        parser.add_argument('Elements of Civil Engineering And Mechanics')
        parser.add_argument('Engineering Graphics')
        parser.add_argument('Engineering Physics Laboratory')
        parser.add_argument('Basic Electrical Engineering Laboratory')
        parser.add_argument('Technical English 1')

        args = parser.parse_args()
        data = np.fromiter(args.values(), dtype=int)
        data = data.reshape(1, -1)
        
        points = model.predict(data)[0]
        final_marks = points_to_marks(points)

        return final_marks, 200

api.add_resource(PerformancePrediction, '/predict')

if __name__ == '__main__':
    app.run(debug=True, port=6000)