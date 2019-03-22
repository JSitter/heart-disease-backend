# Heart Disease Predictor Backend

This project is the backend for the heart disease predictor.

This project will use a Django backend with MLQ to serve predictions for heart disease to the front end. The anonymized user data is stored in a NoSQL database.

## Database Models

### User
* id: This is the user id
* age: Int
* sex: Int
* cp: Int
* trestbps: Int
* chol: Int
* fbs: Int
* restecg: Int
* thalach: Int
* exang: Int
* oldpeak: Float
* slope: Int
* ca: Int
* thal: Int
* prediction: String

### Backend Routes
#### POST : '/predict/
  age: Int
  sex: Int
  cp: Int
  trestbps: Int
  chol: Int
  fbs: Int
  restecg: Int
  thalach: Int
  exang: Int
  oldpeak: Float
  slope: Int
  ca: Int
  thal: Int
  prediction: String