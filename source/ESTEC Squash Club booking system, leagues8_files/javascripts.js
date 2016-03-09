// JavaScript Document
//if(self==top){document.documentElement.style.visibility='visible'}else{top.location=self.location};
if(top != self) top.location.replace(location);
  
function clearTxt(txt,x){
	if (x.value == txt) x.value = '';
}

function resetTxt(txt,x){
if (x.value == '') x.value = txt;
}

function popup(url){
	var xleft = (window.screen.width/2)-(950/2)-10;
	var xtop = (window.screen.height/2)-(500/2)-60; //15;
	var newwin = window.open(url,'cms_window','channelmode=no,location=no,scrollbars=no,left='+xleft+',top='+xtop+',width=950,height=600,status=1')
	newwin.focus();
}

function max_chars(field,msg_span){
	var chars = field.value.length;
	var span = document.getElementById(msg_span);
	var msg = " characters left.";
	if ( chars == 0 ) { x = 4000 } 
	if ( chars > 0 ) { x = (4000-chars) } 
	if ( chars >= 4000 ) { field.value = field.value.substring(0,4000); x = 0 }
	span.innerHTML = x.toString() + msg;
	}
	
function isEmail(s){
	if (s.search(/^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]{2,4}$/) != -1)
		return true ;
	else
		return false ;
	}
	
function maxchars(field,msg_span,limit){
	var chars = field.value.length;
	var span = document.getElementById(msg_span);
	var msg = " characters left";
	if ( chars == 0 ) { x = limit } 
	if ( chars > 0 ) { x = (limit-chars) } 
	if ( chars >= limit ) { field.value = field.value.substring(0,limit); x = 0 }
	span.innerHTML = x.toString() + msg;
	}
	
function show_image(imgID) { 
	document.getElementById("showimage").style.backgroundImage="none";
	document.getElementById("showimage").style.backgroundImage="url(imgs/230/"+ imgID +".jpg)";
	window.location = window.location.toString().replace('#showimage_anchor','') + "#showimage_anchor";
	} 
	
function showhide(divID) {
	div = document.getElementById(divID); 
	div.style.display = (div.style.display == 'block') ? 'none' : 'block';
	} 
