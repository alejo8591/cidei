$(document).ready(function(){
	$('#submit').on('click', function(){
		$.ajax({
			type: "GET",
			url : "drink_info.json",
			dataType : "json",
			success: function(data){
				var drinks = '<ul>';
				$.each(data, function(i, n){
					drinks+='<li>'+n["optiontext"]+'</li>';
				});
				drinks+='</ul>';
				$('#message').append(drinks);
			}
			return false;
		});
	});
});