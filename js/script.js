var lock = false;

		$(document).ready(function(){
			$("#logo").click(
  				function(e){
  					if(!lock)
  					{
	  					lock=true;
	  					$(this).animate({marginTop: '-50px'}, 1000);
	  					$("#subtext").hide();
	  					$("#navBar").animate({marginTop:"45%"} , 1000);
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

  				$("#bCircle").animate({marginLeft:"220px",opacity:1},800);
  				$("#gCircle").animate({marginLeft:"320px",opacity:1},1000);
  				$("#pCircle").animate({marginLeft:"420px",opacity:1},1200);
  				$("#rCircle").animate({marginLeft:"520px",opacity:1},1400);
  			}

  			function morphCircles()
  			{
				$("#bCircle").animate({width:"8px",height:"200px"},400);
  				$("#gCircle").animate({width:"8px",height:"400px"},600);
  				$("#pCircle").animate({width:"8px",height:"300px"},800);
  				$("#rCircle").animate({width:"8px",height:"150px"},1000);  				
  			}
		
		