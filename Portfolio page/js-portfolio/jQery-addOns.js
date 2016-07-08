$(document).ready(function(){
	$(".portfolio-item").mouseenter(function(){
		$(this).find("img, h3").removeClass("hide");
		$(this).find(".main-img").fadeTo("fast", 0.1);
	});
	$(".portfolio-item").mouseleave(function(){
		$(this).find("img, h3").addClass("hide");
		$(this).find(".main-img").removeClass("hide")
		$(this).find(".main-img").fadeTo("fast", 1);
	});
});


$(document).ready(function(){
	$("#Portfolio-link").click(function(){
		$('html,body').animate({
  	 		scrollTop: $("#Portfolio").offset().top -30
		});
	});

	$("#Experience-link").click(function(){
		$('html,body').animate({
  	 		scrollTop: $("#Experience").offset().top -30
		});
	});

	$("#Achievements-link").click(function(){
		$('html,body').animate({
  	 		scrollTop: $("#Achievements").offset().top -30
		});
	});

	$("#Education-link").click(function(){
		$('html,body').animate({
  	 		scrollTop: $("#Achievements").offset().top -30
		});
	});
});