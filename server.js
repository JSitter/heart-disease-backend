let exress = require('express');
let app = express();

app.post((req, res)=>{
  res.send('Route Test');
})

app.set('port', process.env.PORT || 8070);

var server = app.listen(app.get('port'), function() {
  console.log('Listening on port ', server.address().port);
});