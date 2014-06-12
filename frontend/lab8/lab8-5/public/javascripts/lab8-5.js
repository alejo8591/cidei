$(document).ready(function(){

  function Validate(){};

  Validate.prototype = {
    email : function(email){
      var pattern = new RegExp(/^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]+$/);
      return pattern.test(email);
    },
    userid : function(uid){
      var pattern = new RegExp(/^[0-9]+$/);
      return pattern.test(uid);
    }
  }

  $('#nid').focus(function(){
    $(this).addClass('inputs');
  });

  $('#username').focus(function(){
    $(this).addClass('inputs');
  });
 
  $('.password').focus(function(){
    $(this).addClass('inputs');
  });

  $('.conf-password').focus(function(){
    $(this).addClass('inputs');
  });
 
  $('.emailadd').focus(function(){
    $(this).addClass('inputs');
  });
  
  $('.nid-error, .user-error, .password-error, .conf-password-error, .email-error, .food-error, .pay-error, .city-error').addClass('error');
  $('.nid-error, .user-error, .password-error, .conf-password-error, .email-error, .food-error, .pay-error, .city-error').hide();
  $('#info').remove();
 
  $('.button').bind('click', function(event){

    $('#info').remove();
    $('#openModal > div').empty();

    var validate = new Validate();

    var data=$('#nid').val();

    if(validate.userid(data)){
      $('#nid').removeClass('error').addClass('success');
      $('.nid-error').hide();
      localStorage.setItem('nid', data);
    }
    else{
      $('#nid').next().show();
      $('input#nid').removeClass('success').addClass('error');
      $('.nid-error').next().show();
      $('.nid-error').text('Indique su Documento de Identidad');
    }

    var data=$('#username').val();

    var len=data.length;
    
    if(len<1 && data === ""){
      $('#username').next().show();
      $('#username').addClass('error');
      $('.user-error').next().show();
      $('.user-error').text('Por favor indique su(s) Nombre(s) y Apellido(s)');
    }
    else{
      $('#username').next().hide();
      $('.user-error').next().hide();
      localStorage.setItem('username', data);
    }
 
    var data=$('.password').val();

    var len=data.length;
    
    if(len<1 && len!==""){
      $('.password').next().show();
      $('input.password').addClass('error');
      $('.password-error').next().show();
      $('.password-error').text('Indique una Contraseña');
    }
    else{
      $('.password').next().hide();
      $('.password-error').next().hide();
    }

    var confData=$('.conf-password').val();

    var len=confData.length;

    if(len<1){
      $('.conf-password').next().show();
      $('.conf-password-error').next().show();
      $('.conf-password-error').text('Confirme la Contraseña');
    }
    else{
      $('.conf-password').next().hide();
      $('.conf-password-error').next().hide();

      if($('.password').val() !== $('.conf-password').val()){
        $('.conf-password').next().show();
        $('.conf-password-error').next().show();
        $('.conf-password-error').text('¡La Contraseña No es igual!');
      }
      else{
        $('.conf-password').next().show();
        $('.conf-password-error').hide();
        localStorage.setItem('password', data);
      }
    }
 
    data=$('.emailadd').val();
    
    if(validate.email(data)){
      // $('.emailadd').next().hide();
      $('.email-error').hide();
      localStorage.setItem('email', data);
    }
    else{
      $('.emailadd').next().show();
      $('.email-error').next().show();
      $('.email-error').text('¡El email es incorrecto!');
    }
 
    var count=0, meals={};
    
    $('#checkboxes').find(':checkbox').each(function(){
      if($(this).is(':checked')){
        count+=parseInt($(this).val());
        meals[$(this).attr('name')] = parseInt($(this).val());
      }
    });
    
    if(count==0){
      $('.food-error').css({'margin':50}).show();
      $('.food-error').text('¡Debe seleccionar un Alimento!');
    }
    else{
      $('.food-error').hide();
      $('.food-total').show();
      $('.food-total').text('Total de la compra: $' + count + ' M/Cte');
      localStorage.setItem('total', count);
      localStorage.setItem('meals', JSON.stringify(meals));
    }
 
    count=0;

    $('#radios').find(':radio').each(function(){
      if($(this).is(':checked')){
        count++;
        localStorage.setItem('paymode', $(this).val());
      }
    });
    if(count==0){
      $('.pay-error').css({'margin-left':50}).show();
      $('.pay-error').text('Debe seleccionar un modo de Pago');
    }
    else{
      $('.pay-error').hide();
    }
 
    count=$('select option:selected').val();
    if(count=="0"){
      $('.city-error').show();
      $('.city-error').text('¡Debe seleccionar una Ciudad!');
    }
    else{
      $('.city-error').hide();
      localStorage.setItem('city', count);
      $('#buttons').append(
        '<a id="info" href="#openModal">Ver Pedido</a>'
      );
      $('.inputs').removeClass('error');
      $('.inputs').addClass('success');
    }
    //event.preventDefault();
  });

  $(document).on('click', '#info', function(){

    $('#openModal > div').append(
      '<a href="#close" title="Close" class="close">X</a>'+
      '<h2>Este es tu pedido</h2>' +
      '<ul>' +
      '<li>Su nombre es: ' + localStorage.getItem('username') + '</li>' +
      '<li>Su documento es: ' + localStorage.getItem('nid') + '</li>' +
      '<li>Su email es: ' + localStorage.getItem('email') + '</li>' +     
      '<li id="listMeals">Los alimentos que Solicita son: <ul></ul></li>' + 
      '<li>El modo de pago es: ' + localStorage.getItem('paymode') + '</li>' +  
      '<li>La ciudad donde habita es: ' + localStorage.getItem('city') + '</li></ul>'  

    );
    var meals =  JSON.parse(localStorage.getItem('meals'));

    $.each(meals, function(key, value){
          $('#listMeals > ul').append('<li>El producto ' + key + ' cuesta $' + value + ' M/Cte</li>');
    });
  });
});