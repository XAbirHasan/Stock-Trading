var menu = document.getElementById("menu");
var sub_menu = document.getElementById("sub_menu");

var hide_block="";

menu.addEventListener("mouseover", sub_menu_display, false);

sub_menu.addEventListener("mouseover", sub_menu_display, false);

menu.addEventListener("mouseout", sub_menu_hide, false);


function sub_menu_display() {

	sub_menu.setAttribute("style", "transform:translate(28%,55%);opacity:1;visibility: visible;");

}

function sub_menu_hide() {
	
   
    sub_menu.setAttribute("style", "transform:translate(28%,100%);opacity:0;visibility: hidden;");
	
}



//social media buttons on load
var wha_soc = document.getElementById("wha-soc");
var ins_soc = document.getElementById("ins-soc");
var face_soc = document.getElementById("face-soc");
var twi_soc = document.getElementById("twi-soc");




window.onload = function()
{
	//adding the event listerner for Mozilla
	if(window.addEventListener){
		
		setTimeout(function() { //social media icon 1
			
			wha_soc.setAttribute("style", "transform:translate(0%,0%) rotate(0deg);transition:all 0.5s;");
			
		}, 400)
		
		setTimeout(function() { //social media icon 2
			
			ins_soc.setAttribute("style", "transform:translate(0%,0%) rotate(0deg);transition:all 0.65s;");
			
		}, 600)
		
		setTimeout(function() { //social media icon 3
			
			face_soc.setAttribute("style", "transform:translate(0%,0%) rotate(0deg);transition:all 0.8s;");
			
		}, 800)
		
		setTimeout(function() { //social media icon 4
			
			twi_soc.setAttribute("style", "transform:translate(0%,0%) rotate(0deg);transition:all 0.95s;");
			
		}, 1000)
		
	}
	
}



























