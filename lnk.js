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

html = "<html> <head> <title>Remote: Page Link bookmarklets</title> <base target="receiver"> <style type="text/css"> body { background-color:  #ffddbb ;  color: black; } a.bml { color : #007700; } .ctg{ color : #000010; } </style> <script type="text/javascript"> function time(){ var start= (new Date); var day = start.getDay(); var mm = start.getMonth(); var yr = start.getYear()+1900; var h = start.getHours(); var m = start.getMinutes(); var hm = (mm + ' \/ ' + day + ' \/ ' + yr + ' \t     ' + h + ' : ' + m); return hm; }; quotes = new Array( ); quotes[quotes.length] = {quote:"One should eat to live, and not live to eat.", author:"Moliere"}; quotes[quotes.length] = {quote:"For man is man and master of his fate.", author:"Tennyson"}; quotes[quotes.length] = {quote:"History is more or less bunk.", author:"Henry Ford"}; quotes[quotes.length] = {quote:"You should never have your best trousers on when you turn out to fight for freedom and truth.", author:"Ibsen"}; quotes[quotes.length] = {quote:"It is vain and foolish to talk of knowing Greek.", author:"Woolf"}; function insertSaying() { var currIndex = Math.floor(Math.random( ) * (quotes.length)); var qt = quotes[currIndex].quote + ' ' + quotes[currIndex].quote; } /*TODO: add selectText to url //TODO: add to category*/ function writeURL(){ /*//var selectText="abcdefgh"; //var data = document.forms[0].selectText.value;*/ var elm = document.createElement("p") elm.className="ctg";	elm.appendChild(document.createTextNode(window.location.href)); document.getElementByID('url-ctg').appendChild(pElem); }  </script> </head> <body> <p><b> <script type="text/javascript"> if(Math.floor(math.random( )>0){ document.write(time())	<a class="bml" href="localhost:8888/dev2.html" onclick="writeURL(); return false;">list</a> </p> <p> <div id='url-ctg'> <script type="text/javascript"> addOnLoadEvent(function() {insertSaying('url-ctg')}; </script> </div> </p> </body> </html>"

document.write(html);
document.close();
