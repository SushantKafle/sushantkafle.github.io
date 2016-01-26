var lock = false;
var width;
var height;

		$(document).ready(function(){
		
			arrangeElements();
			
			$(window).resize(function(){
				arrangeElements();
			});
			
			$("#logo").click(
  				function(e){
  					if(!lock)
  					{
	  					lock=true;
	  					$(this).animate({marginTop: -(0.6*height)}, 1000);
	  					$("#subtext").hide();
	  					$("#navBar").animate({marginTop:(height+(0.55*height))} , 1000);
	  					$("#text").css({opacity:1});
	  					animateCircles();
	  					morphCircles();
	  					showLabels();
	  					
	  				}

  					
  				});
			
			$("#AcPro").mouseover(function(){
					$(this).html("[ About me ]");
				});

			$("#AcPro").mouseout(function(){
					$(this).html("&nbsp;&nbsp;About me&nbsp;&nbsp;");
				});
            
            $("#AcPro").click(function(){
              /*  
              $('#text').css('color','rgb(0,162,232)');
            //    $('body').css('background', '#ffcb00');
                
                $("#gCircle").hide();
                $("#rCircle").hide();
                $("#pCircle").hide();
                
                $("#NaPro").hide();
                $("#AcPro").hide();
                $("#Desg").hide();
                $("#Oth").hide();
                
                bodyAnimate($("#bCircle"));
               */

               window.location = 'http://kaflesushant.com.np/plain/';
            });
            
            $("#NaPro").click(function(){
                /*
                $('#text').css('color','rgb(67,192,123)');
          //      $('body').css('background', '#ffcb00');
                
                $("#bCircle").hide();
                $("#rCircle").hide();
                $("#pCircle").hide();
                
                $("#NaPro").hide();
                $("#AcPro").hide();
                $("#Desg").hide();
                $("#Oth").hide();
                
                bodyAnimate($("#gCircle"));
                */
                window.location = 'http://kaflesushant.com.np/plain/CV/cv.pdf';
            });
            
            $("#Desg").click(function(){
                /*
                $('#text').css('color','rgb(112,146,190)');
  //              $('body').css('background', '#ffcb00');
                
                $("#gCircle").hide();
                $("#rCircle").hide();
                $("#bCircle").hide();
                
                $("#NaPro").hide();
                $("#AcPro").hide();
                $("#Desg").hide();
                $("#Oth").hide();
                
                bodyAnimate($("#pCircle"));
                */
                window.location = 'http://kaflesushant.com.np/plain/#projects';
            });
            
            
            $("#Oth").click(function(){
                /*
			    $('#text').css('color','rgb(224,35,97)');
//                $('body').css('background', '#ffcb00');
                
                $("#gCircle").hide();
                $("#pCircle").hide();
                $("#bCircle").hide();
                
                $("#NaPro").hide();
                $("#AcPro").hide();
                $("#Desg").hide();
                $("#Oth").hide();
                
                bodyAnimate($("#rCircle"));
                */
            });
            

			$("#NaPro").mouseover(function(){
					$(this).html("[ Curriculum Vitae ]");
				});

			$("#NaPro").mouseout(function(){
					$(this).html("&nbsp;&nbsp;Curriculum Vitae&nbsp;&nbsp;");
				});

			$("#Desg").mouseover(function(){
					$(this).html("[ Projects ]");
				});

			$("#Desg").mouseout(function(){
					$(this).html("&nbsp;&nbsp;Projects&nbsp;&nbsp;");
				});

			$("#Oth").mouseover(function(){
					$(this).html("[ Contact ]");
				});

			$("#Oth").mouseout(function(){
					$(this).html("&nbsp;&nbsp;Contact&nbsp;&nbsp;");
				});

  		});
		
		jQuery.fn.textWidth = function(){
			var _t = jQuery(this);
			var html_org = _t.html();
			if(_t[0].nodeName=='INPUT'){
				html_org = _t.val();
			}
			var html_calcS = '<span>' + html_org + '</span>';
			jQuery('body').append(html_calcS);
			var _lastspan = jQuery('span').last();
			_lastspan.css({
				'font-size' : _t.css('font-size')
				,'font-family' : _t.css('font-family')
			})
			var width =_lastspan.width() + 5;
			_lastspan.remove();
			return width;
		}
        
        function bodyAnimate($circle)
        {
            $circle.animate({width:"20px",height:"20px",marginTop:"130px"},400);
            $circle.animate({width:"2000px",marginLeft:"-700px",height:"5px"},600);
            
            $("#mainBody").show();
            $("#mainBody").css({marginTop:"520px",marginLeft:"100px"},400);
        }
		
		function arrangeElements()
		{
			width=$(window).width();
			height=window.innerHeight;
			
			
            $("#mainBody").hide();
            
			var textLeftMargin=(width/2)-($("#text").textWidth()/2);
			var textTopMargin=height - 0.4 * height;
			
			var textLeftMarginSudo = textLeftMargin + 10;
			
			var navBarLeftMargin=(width/2)-70;
			var navBarTopMargin=(height - 0.05* height);
			
			var circleLeftMargin=textLeftMargin-115;
			var circleTopMargin=textTopMargin-50;
			
			var subTextLeftMargin=textLeftMargin+($("#text").textWidth()/2)+130;
			var subTextTopMargin=textTopMargin+70;
			
			var AcProLeftMargin=textLeftMargin - 0.02 * textLeftMargin;
			var NaProLeftMargin=textLeftMargin + 0.1*textLeftMargin;
			var DesgLeftMargin=textLeftMargin + 0.6 * textLeftMargin;
			var OthLeftMargin=textLeftMargin + 0.95 *textLeftMargin;
			
			
		if(!lock){
				$("#text").css({marginTop:textTopMargin});
				$("#navBar").css({marginTop:navBarTopMargin});
				$("#circles").css({marginTop:circleTopMargin});
				$("#subtext").css({marginTop:subTextTopMargin});
				$("#circles").css({marginLeft:circleLeftMargin});
			}
			
			$("#text").css({marginLeft:textLeftMarginSudo});
			$("#navBar").css({marginLeft:navBarLeftMargin});
			$("#circles").css({marginLeft:circleLeftMargin});
			$("#subtext").css({marginLeft:subTextLeftMargin});
			$("#AcPro").css({marginLeft:AcProLeftMargin});
			$("#NaPro").css({marginLeft:NaProLeftMargin});
			$("#Desg").css({marginLeft:DesgLeftMargin});
			$("#Oth").css({marginLeft:OthLeftMargin});

		}

		function showLabels()
		{
			$("#AcPro").delay(1500).show(0);
			$("#NaPro").delay(1900).show(0);
			$("#Desg").delay(2100).show(0);
			$("#Oth").delay(2400).show(0);
		}

		function animateCircles()
		{
			$("#bCircle").animate({width:"30px",height:"30px",marginTop:"125px"},400);
			$("#gCircle").animate({width:"30px",height:"30px",marginTop:"125px"},600);
			$("#pCircle").animate({width:"30px",height:"30px",marginTop:"125px"},800);
			$("#rCircle").animate({width:"30px",height:"30px",marginTop:"125px"},1000);

			$("#bCircle").animate({marginLeft:"160px",opacity:1},800);
			$("#gCircle").animate({marginLeft:"280px",opacity:1},1000);
			$("#pCircle").animate({marginLeft:"400px",opacity:1},1200);
			$("#rCircle").animate({marginLeft:"520px",opacity:1},1400);
		}

		function morphCircles()
		{
			$("#bCircle").animate({width:"8px",height:"200px"},400);
			$("#gCircle").animate({width:"8px",height:"400px"},600);
			$("#pCircle").animate({width:"8px",height:"300px"},800);
			$("#rCircle").animate({width:"8px",height:"150px"},1000);  				
		}

	
		
