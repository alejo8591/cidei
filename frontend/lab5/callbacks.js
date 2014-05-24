/* Callbacks en JS */
/*
Un callback es un una funcion, que por parametro se le envia otra 
funcion, y la funcion que lo recibe, espera a que se ejecute 
esa funcion
*/
function algo(miCallback){
	miCallback();
}

algo(function(){
	console.log("Esto es un callback");
});


function otroCallback(miCallback){
	miCallback('Un argumento');
}

otroCallback(function(unValor){
	console.log('Algo se imprime y es: '+ unValor);
});
