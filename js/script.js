$(function() {
  $('a[href*=#]').on('click', function(e) {
    e.preventDefault();
    $('html, body').animate({ scrollTop: $($(this).attr('href')).offset().top}, 500, 'linear');
  });
});

(function($) {          
    $(document).ready(function(){ 
    	$('#header').hide();    	                   
        $(window).scroll(function(){                          
            if ($(this).scrollTop() > 500) {
                $('#header').show(200);
            } else {
                $('#header').fadeOut(200);
            }
        });
    });
})(jQuery);
