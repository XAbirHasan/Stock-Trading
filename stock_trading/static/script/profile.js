var menu = document.getElementById("menu");
var sub_menu = document.getElementById("sub_menu");

var hide_block = "";

menu.addEventListener("mouseover", sub_menu_display, false);

sub_menu.addEventListener("mouseover", sub_menu_display, false);

menu.addEventListener("mouseout", sub_menu_hide, false);


function sub_menu_display() {

	sub_menu.setAttribute("style", "transform:translate(28%,55%);opacity:1;visibility: visible;");

}

function sub_menu_hide() {


	sub_menu.setAttribute("style", "transform:translate(28%,100%);opacity:0;visibility: hidden;");

}
















