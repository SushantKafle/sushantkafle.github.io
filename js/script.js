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
	  					$("#navBar").animate({marginTop:(height+(0.5*height))} , 1000);
	  					$("#text").css({opacity:1});
	  					animateCircles();
	  					morphCircles();
	  					showLabels();
	  					
	  				}

  					
  				});
			
			$("#AcPro").mouseover(function(){
					$(this).html("{ Academic Projects }");
				});

			$("#AcPro").mouseout(function(){
					$(this).html("&nbsp;&nbsp;Academic Projects&nbsp;&nbsp;");
				});

			$("#NaPro").mouseover(function(){
					$(this).html("{ Non-Academic Projects }");
				});

			$("#NaPro").mouseout(function(){
					$(this).html("&nbsp;&nbsp;Non-Academic Projects&nbsp;&nbsp;");
				});

			$("#Desg").mouseover(function(){
					$(this).html("{ Designs }");
				});

			$("#Desg").mouseout(function(){
					$(this).html("&nbsp;&nbsp;Designs&nbsp;&nbsp;");
				});

			$("#Oth").mouseover(function(){
					$(this).html("{ Others }");
				});

			$("#Oth").mouseout(function(){
					$(this).html("&nbsp;&nbsp;Others&nbsp;&nbsp;");
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
		
		function arrangeElements()
		{
			width=$(window).width();
			height=window.innerHeight;
			
			var textLeftMargin=(width/2)-($("#text").textWidth()/2);
			var textTopMargin=height - 0.4 * height;
			
			var navBarLeftMargin=(width/2)-70;
			var navBarTopMargin=(height - 0.1 * height);
			
			var circleLeftMargin=textLeftMargin-115;
			var circleTopMargin=textTopMargin-50;
			
			var subTextLeftMargin=textLeftMargin+($("#text").textWidth()/2)+130;
			var subTextTopMargin=textTopMargin+70;
			
			var AcProLeftMargin=(width/2)-($("#AcPro").textWidth()/2) - 120;
			var NaProLeftMargin=(width/2)-($("#NaPro").textWidth()/2) - 10;
			var DesgLeftMargin=(width/2)-($("#Desg").textWidth()/2) + 75;
			var OthLeftMargin=(width/2)-($("#Oth").textWidth()/2) + 180;
			
			
		if(!lock){
				$("#text").css({marginTop:textTopMargin});
				$("#navBar").css({marginTop:navBarTopMargin});
				$("#circles").css({marginTop:circleTopMargin});
				$("#subtext").css({marginTop:subTextTopMargin});
				$("#circles").css({marginLeft:circleLeftMargin});
			}
			
			$("#text").css({marginLeft:textLeftMargin});
			$("#navBar").css({marginLeft:navBarLeftMargin});
			$("#circles").css({marginLeft:circleLeftMargin});
			$("#subtext").css({marginLeft:subTextLeftMargin});
			$("#AcPro").css({marginLeft:AcProLeftMargin-5});
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

			$("#bCircle").animate({marginLeft:"180px",opacity:1},800);
			$("#gCircle").animate({marginLeft:"280px",opacity:1},1000);
			$("#pCircle").animate({marginLeft:"380px",opacity:1},1200);
			$("#rCircle").animate({marginLeft:"480px",opacity:1},1400);
		}

		function morphCircles()
		{
			$("#bCircle").animate({width:"8px",height:"200px"},400);
			$("#gCircle").animate({width:"8px",height:"400px"},600);
			$("#pCircle").animate({width:"8px",height:"300px"},800);
			$("#rCircle").animate({width:"8px",height:"150px"},1000);  				
		}
	
		
