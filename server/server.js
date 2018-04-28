var express = require('express');
var queryString = require('query-string');
var request = require('request');
var bodyParser = require('body-parser');
var deploy = require('./deploy');
var app = express();

app.use(bodyParser.json());


app.post('/github/push', function (req, res) {
    deploy(req.body);
    res.send(null);
});

app.use(express.static('public'));


app.listen(80, () => { console.log("Application start"); });
