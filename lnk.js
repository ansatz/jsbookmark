//*#quotes
//#links
//#books
//#tags
//#friend-net xfn
//#encrypt
//#backup
//#expandable-menu.js
//#p309
//*/


//html= "<html>\n<head>\n<title>Remote: Page Link bookmarklets</title> <base target=\"receiver\"> <style type=\"text/css\"> body { background-color:  #ffddbb ;  color: black; } a.bml { color : #007700; } </style> <script text=\"\/javascript\"> function time(){ var start= (new Date); var day = start.getDay(); var mm = start.getMonth(); var yr = start.getYear()+1900; var h = start.getHours(); var m = start.getMinutes(); var hm = (mm + ' \/ ' + day + ' \/ ' + yr + ' \t     ' + h + ' : ' + m + '<br>remote to start server'); return hm; }; </script> </head> <body> <p><b> <script text=\"\/javascript\"> document.write(time())	</script></b</p> <p><b><a href=\"http:\/\/localhost:8888\/dev2.html\">LINKS:</a></b></p> <p> <a class=\"bml\" href=\"javascript:(function(){url = encodeURI(window.location.href);alert(url);})()\">location</a></head></html>"; 

//"<html>\n<head>\n<title>Remote: Page Link bookmarklets</title> <base target=\"receiver\"> <style type=\"text/css\"> body { background-color:  #ffddbb ;  color: black; } a.bml { color : #007700; } </style> </head> <body> <p><b><a href=\"http:\/\/localhost\/dev2.html\">links</a></b></p> <p> <a class=\"bml\" href=\"javascript:(function(){url=encodeURI(window.location.href);alert(url);})()\">location</a></head></html>"; 


document.write(html);
document.close();
