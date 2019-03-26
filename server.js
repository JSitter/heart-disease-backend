const express = require('express');
const app = express();
const fs = require('fs');
app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});
app.get('/', (req, res)=>{
  fs.readFile('./datasets/saved.csv', 'utf8', function(err, contents){
    if(err){
      console.log(err)
      res.send(err)
    }else{
      res.send(contents)
    }

  })

})

app.set('port', process.env.PORT || 8070);

var server = app.listen(app.get('port'), function() {
  console.log('Listening on port ', server.address().port);
});
