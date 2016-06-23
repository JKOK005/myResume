$(document).ready(function(){
	//My story toggle function
	$('.myButton').click(function(){
		$(".showMore").toggleClass('hide');
		if ($(this).text().trim() == "My story"){
			$(this).text('Hide');
		}
		else if ($(this).text().trim() == "Hide"){
			$(this).text('My story');
		}
	});

});

function show_skills(skills){
	// Function to show only 1 selected skill
	var i;
	for(i=0; i<skills.length; i++){
		if(skills[i] == true){
			$('.paragraph').eq(i).removeClass('hide');
		}
		else{
			$('.paragraph').eq(i).addClass('hide');
		}
	}
}

$(document).ready(function(){
	//Software skills toggle function
	var skills = [false,false,false,false,false,false];
	$("#Software > img").click(function(){
		var num = $("#Software > img").index(this);
		var i;

		for(i=0; i<skills.length; i++){
			if (i == num){
				skills[i] = !skills[i];	// Toggle
			}
			else{
				skills[i] = 0;			// Turn off
			}
		}
		show_skills(skills);
	});

});

