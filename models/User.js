const mongoose = require('mongoose');
const Schema = mongoose.Schema;

var User = new Schema({
  age: Int,
  sex: Int,
  cp: Int,
  trestbps: Int,
  chol: Int,
  fbs: Int,
  restecg: Int,
  thalach: Int,
  exang: Int,
  oldpeak: Float,
  slope: Int,
  ca: Int,
  thal: Int,
  prediction: String,
});

module.exports = mongoose.model('User', User);