var express = require('express'),
	app = express(),
	http = require('http'),
	server = http.createServer(app),
	io = require('socket.io')(server);
	port = process.env.PORT || 8585;

server.listen(port, function(){
	console.log('Listen %d', port);
});

app.use(express.static(__dirname));

// Ruta(s) que se manejaran
app.get('/', function(req, res){
	res.sendfile(__dirname + '/index.html');
});

// variable `usernames` para los usuarios conectados
var usernames = {};

io.sockets.on('connection', function(socket){
	// Cuando el cliente, browser, emite el evento `sendchat`, este debe escuchar y ejecutar
	socket.on('sendchat', function(data){
		// Le enviamos `emit` al cliente que ejecute `updatechat` con dos paramtros `socket.usernme` y `data`
		io.sockets.emit('updatechat', socket.username, data);
	});
	// Cuando el cliente emite un evento `adduser`, este escucha y ejecuta
	socket.on('adduser', function(username){
		// Almacenamiento del nombre de usuario en la sesión de toma de info del cliente
		socket.username = username;
		// Adicionamos el usuario `socket.username` al objeto `usernames`
		usernames[username] = username;
		// enviamos al cliente el objeto con la listas de usuarios en el objeto `usernames`
		socket.broadcast.emit('updatechat', 'SERVER', username + ' Esta conectado');
		// enviamos petición al mismo cliente de la petición con la conexión de el mismo
		socket.emit('updatechat', 'SERVER', 'Usted esta conectado');
		// actulizamos la lista de usuarios en el chat, en el cliente
		io.sockets.emit('updateusers', usernames);
	});

	// cuando el usuario se desconecta
	socket.on('disconnect', function(){
		delete usernames[socket.username];
		// Actualizamos la de usuarios en el cliente
		io.sockets.emit('updateusers', usernames);
		// Envio global de la actualización de la lista de clientes conectados
		socket.broadcast.emit('updatechat', 'SERVER', socket.username + ' Esta desconectado');
	});
});
