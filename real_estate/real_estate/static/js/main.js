const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();


// Alert messages fadeout in 3 sec
setTimeout(function() {
  $('#message').fadeOut('slow');
}, 3000);
