
$min = $("#min th").text();
$second = $("#second th").text();
$switch = $("#contrl button").text();
var  on = true;
var off = false;
var flag = off;
var timer;

$("button").click(function (){

	flag = !flag;
	
	if(flag == on ){
		$("#contrl button").text("停止");
		timer = setInterval(function(){
		
		$second--;
		// $("#second th").text($second);
		
		$("#second th").text($second);
		$("#min th").text($min);
		if($second == 0){
			$second = 60;
			$min--;
		}
	
		},1000);

	} else {
		
		clearInterval(timer);
		$("#contrl button").text("启动");
	}
});