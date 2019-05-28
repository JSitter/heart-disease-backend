from flask_restplus import Api, Resource, fields, reqparse
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import random
from sklearn.externals import joblib
from pymongo import MongoClient
import logging


log_reg_model = joblib.load('logistic_saved.h5')


app = Flask(__name__)
client = MongoClient('mongodb://mongodb:27017/heartdisease')
CORS(app)
api = Api(app, version='1.0', title='Heart Disease Predictor', description='This is a flask app that predicts heart disease based on the UCI dataset.')
ns = api.namespace('api', description='Api endpoints for predictions')

single_parser = api.parser()

parser = reqparse.RequestParser()

@ns.route('/')
class Index(Resource):
  ''' Main page.'''
  @api.doc(parser=single_parser, description='Get main page')
  def get(self):
    return "Welcome to Heart Disease!"

@ns.route('/predict/')
class LogisticPrediction(Resource):
  @api.doc(parser=single_parser, description='Post Patient data to recieve prediction.')
  def post(self):
    '''Post patient data return predicted true or false.'''
    parser.add_argument('age')
    parser.add_argument('sex')
    parser.add_argument('cp')
    parser.add_argument('trestbps')
    parser.add_argument('thalach')
    parser.add_argument('exang')
    parser.add_argument('oldpeak')
    parser.add_argument('slope')
    args = parser.parse_args()

    values = [
        float(args.age),
        float(args.sex),
        float(args.cp),
        float(args.trestbps),
        float(args.thalach),
        float(args.exang),
        float(args.oldpeak),
        float(args.slope),
    ]

    # logging.warning(args)

    prediction = log_reg_model.predict([values])[0]
    # return jsonify({'target':random.randint(0,1)})

    return jsonify({'target':int(prediction)})
    # return jsonify({'target': })

# @app.errorhandler(404)
# def not_found(resource):
#     return jsonify({'error': '404'})

if __name__ == '__main__':

  PORT = int(os.environ.get('PORT', 8001))
  app.run(host='0.0.0.0', port=PORT)
