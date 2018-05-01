var express = require('express');
var path = require('path');
var bodyParser = require('body-parser');
var deploy = require('./deploy');
var app = express();

app.use(bodyParser.json());


app.post('/github/push', function (req, res) {
    deploy(req.body);
    res.send(null);
});

app.get('/force/:input', function (req, res) {
    res.sendFile(path.join(__dirname, 'public', 'ImpressiveACDC', 'visualization.html'));
});

app.get('/consistent/:input', function (req, res) {
    res.sendFile(path.join(__dirname, 'public', 'ImpressiveACDC', 'consistent-cluster', 'visualization.html'));
});

app.use(express.static('public'));


app.listen(80, () => { console.log("Application start"); });
