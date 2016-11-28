206 121    167 121
126 124    86 124




144 125  105 125
59 15

86 76


26 73
var wLeft = []
var lLeft = []
wOneX   = -144
wOneY   = -125
wTwoX   = -105
wTwoY   = -125
wThreeX = -59
wThreeY = 15


wFourX  = -26
wFourY  = -73

wFiveX  = 26
wFiveY  = -73

wSixX  = 2
wSixY  = -50
wSevenX  = -86
wSevenY  = 76

iOneX   = -206
iOneY   = -121
iTwoX   = -167
iTwoY   = -121
iThreeX = -86
iThreeY = 124
iFourX  = -126
iFourY  = 124


jump(iOneX,iOneY)
goto(iTwoX,iTwoY)
goto(iThreeX,iThreeY)
goto(iFourX,iFourY)
goto(iOneX,iOneY)

jump(wOneX,wOneY)
goto(wTwoX,wTwoY)
goto(wThreeX,wThreeY)
goto(wFourX,wFourY)
goto(wFiveX,wFiveY)
goto(-wThreeX,wThreeY)
goto(-wTwoX,wTwoY)
goto(-wOneX,wOneY)
goto(-wSevenX,wSevenY)
goto(50,77)
goto(0,50)
goto(-50,77)
goto(-83,77)


goto(-iOneX,iOneY)
goto(-iTwoX,iTwoY)
goto(-iThreeX,iThreeY)
goto(-iFourX,iFourY)
goto(-iOneX,iOneY)


var canvas = document.getElementById("id-canvas");
//简单地检测当前浏览器是否支持Canvas对象，以免在一些不支持html5的浏览器中提示语法错误
if(canvas.getContext){
    //获取对应的CanvasRenderingContext2D对象(画笔)
    var ctx = canvas.getContext("2d");

    //设置字体样式
    ctx.font = "30px Courier New";
    //设置字体填充颜色
    ctx.fillStyle = "blue";
    //从坐标点(50,50)开始绘制文字
    ctx.fillText("CodePlayer+中文测试", 50, 50);
}
