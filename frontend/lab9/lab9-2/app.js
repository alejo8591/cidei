/**
 * @requires express
 * @requires createServer
*/
var path = require('path');
var express = require('express');
var app = express();
var http = require('http');
var server = http.createServer(app);
var bodyParser = require('body-parser');
var port = 8585;

server.listen(port, function(){
	console.log('Listen %d', port);
});
/**
 * @memberof express
*/
app.use(bodyParser.json());

/**
 * @memberof express for statics files
 */
app.use(express.static(path.join(__dirname, 'dist')));

app.get('/', function(req, res){
	res.sendfile(__dirname + '/index.html');
});

/**
 * @param {object} req 
 * @param {object} res
 */
app.post('/values', function(req, res){
	/** @var {object} obj */
	var obj = {};
	console.log('body' + JSON.stringify(req.body));
	/** @return  {object} return JSON object */
	res.send(req.body);
});