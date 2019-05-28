from flask_restplus import Api, Resource, fields
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import random
from sklearn.externals import joblib

log_reg_model = joblib.load('logistic_saved.h5')


app = Flask(__name__)
CORS(app)
api = Api(app, version='1.0', title='Heart Disease Predictor', description='This is a flask app that predicts heart disease based on the UCI dataset.')
ns = api.namespace('api', description='Api endpoints for predictions')

single_parser = api.parser()

@ns.route('/')
class Index(Resource):
  ''' Main page.'''
  @api.doc(parser=single_parser, description='Get main page')
  def get(self):
    return "Welcome to Heart Disease!"

@ns.route('/predict')
class LogisticPrediction(Resource):
  @api.doc(parser=single_parser, description='Post Patient data to recieve prediction.')
  def post(self):
    '''Post patient data return predicted true or false.'''
    print(single_parser)
    args = single_parser.parse_args()
    print("hello")
    print(args)
    return jsonify({'target':random.randint(0,1)})

# @app.errorhandler(404)
# def not_found(resource):
#     return jsonify({'error': '404'})

if __name__ == '__main__':

  PORT = int(os.environ.get('PORT', 8001))
  app.run(host='0.0.0.0', port=PORT)
