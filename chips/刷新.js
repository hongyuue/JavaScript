var timeid = setInterval("clickBB()","2000");

var clickBB = function() {
    location.reload([true])
    var $allowButton =  $('button[id ^= allow]')
    if($allowButton.length != 0 ) {
        $("button").click(function() { $allowButton.css("color","red") } )
        $allowButton.trigger("click")
    }
}

// var $allowButton =  $('button[id ^= allow]')
// $("button").click(function() { $allowButton.css("color","red") } )
// $allowButton.trigger("click")

// allowButton.click(function() {
//      allowButton.click.css("background-color","yellow");
//     } )
// // allowButton.click.css("background-color","yellow");
// var clickButton = function() {
//
// }
var request = function(paras){
  var url = location.href;
  var paraString = url.substring(url.indexOf("?")+1,url.length).split("&");
  var paraObj = {}
  for (i=0; j=paraString[i]; i++){
    paraObj[j.substring(0,j.indexOf("=")).toLowerCase()] = j.substring(j.indexOf("=")+1,j.length);
  }
  var returnValue = paraObj[paras.toLowerCase()];
  if(typeof(returnValue)=="undefined") {
    return "";
  }else {
    return returnValue;
  }
}
var theurl=request('url');
