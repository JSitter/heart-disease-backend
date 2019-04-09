from flask_restplus import Api, Resource, fields
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
api = Api(app, version='1.0', title='Heart Disease Predictor', description='This is a flask app the predicts heart disease based on the UCI dataset.')
ns = api.namespace('api', description='Api endpoints for predictions')

single_parser = api.parser()

@ns.route('/')
class Index(Resource):
  ''' Main page.'''
  @api.doc(parser=single_parser, description='Get main page')
  def get(self):
    return "I'm Feeling Fine -- Really..."
  
@ns.route('/predict')
class LogisticPrediction(Resource):
  @api.doc(parser=single_parser, description='Post Patient data to recieve prediction.')
  def post(self):
    '''Post patient data return predicted true or false.'''
    args = single_parser.parse_args()
    print(args)
    return True

if __name__ == '__main__':
  PORT = int(os.environ.get('PORT', 8000))
  app.run(host='0.0.0.0', port=PORT)