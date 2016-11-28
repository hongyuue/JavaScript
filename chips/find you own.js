var can = document.getElementById('id-canvas')
can.width = "800"

document.getElementById('id-canvas').height = "800"
document.getElementById('button-run').onmouseover


var keyDown = function(e) {

    var key = e.witch
    var direction = 1
    var keycode = String(e.which);
    // alert(typeof keycode)
    controlTrangle(keycode)
}


var controlTrangle = function(direction) {
    var angle
    switch(direction){
      case '119':
        angle = 90
        break;
      case '115':
        angle = -90
        break;
      case '97':
        angle = 180
        break;
      case '100':
        angle = 0
        break;
      default:
        angle = 1
    }
    //
    if(angle != 1 && POWER == true) {
        POWER = false
        penup()
        setHeading(angle)
        //
        forward(50)
        POWER = true
    }
}
//计算每次运动后三角形坐标
var trangleCoordinate = function (angle, step) {

    switch(angle){
      case 90:
        source[0] -= step
        break;
      case -90:
        source[0] += step
        break;
      case 180:
        source[1] -= step
        break;
      case 0:
        source[0] += step
        break;
    }
}

//判断碰撞路径
var judgeThePath = function() {

}

var square = function(x, y, l) {
    jump(x, y)
    setHeading(0)
    var i = 1
    while(i < 5) {
      console.log(i)
      i = i + 1
      forward(l)
      right(90)
    }
}
var createEnemys = function(enemysNumber) {
    var i = 0
    var enemysCoordinate = new Array()
    while(i < enemysNumber) {
      var x = randomIntNum(30)
      var y = randomIntNum(40)
      enemysCodiration[i] = x
      enemysCodiration[i + enemysCodiration] = y
      square(x, y, 20)
      i = i + 1
    }
    return enemysCodiration
}
var randomIntNum = function(range) {
    var random = Math.floor(10 - (Math.random() * 20))
    console.log(random)
    return random * range
}
var drawBound = function() {
    jump(-300, -400)
    goto(-300,  400)
    goto( 300,  400)
    goto( 300, -400)
    goto(-300, -400)
}
var initTheMap = function(plies) {
    POWER = false
    drawLines(plies)
    drawBound()
    initTheTrangle(source,90)
}

var initTheTrangle = function(source, angle) {
    setHeading(angle)
    jump(source[0], source[1])
    // trangleCoordinate(angle, 50)
    POWER = true
}

window.onkeypress = keyDown;
var source = [0, 350];
var POWER = false;
var linesPosition = [];
initTheMap(10);
