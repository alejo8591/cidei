var socket = io.connect('http://127.0.0.1:8585');

// En conexión con el servidor, pregunta el respectivo nombre de usuario y una devolución anonima de llamado
socket.on('connect', function(){
	// Llamando al evento, funcion `adduser` y le enviamos un parametro ingresado por el prompt
	socket.emit('adduser', prompt('Cual es su nombre de usuario'));
});
// Evento que esta escuchando la invocación de `updatechat` y actualiza el cuerpo del chat
socket.on('updatechat', function(username, data){
	$('#conversation').append('<b>' + username + ':</b>' + data + '<br />');
});

// Evento que esta escuchando la invocación de `updateusers`, este actualiza la lista de usuarios
socket.on('updateusers', function(data){
	$('#users').empty();
	$.each(data, function(key, value){
		$('#users').append('<div>' + key + '</div>');
	});
});

$(document).ready(function(){
	$('#datasend').click(function(){
		var message = $('#data').val();
		// Indicarle al servidor que ejecute el evento `sendchat` y se le envian dos parametros
		socket.emit('sendchat', message);
	});

	// cuando el usuario utiliza la tecla ENTER
	$('#data').keypress(function(event){
		if(event.which === 13){
			$(this).blur();
			$('#datasend').focus().click();
		}
	});
});





