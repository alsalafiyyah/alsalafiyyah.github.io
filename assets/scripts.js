//<![CDATA[
$(document).ready(function() {

	//check for deeplink
	var deepLink = window.location.hash; 
	
	//cache all tab nodes, hide tabcontent
	var tl = $("#tabs li a");
	var tc = $(".tabContent");
	tc.hide();
	
	//set active Tab and content
	if (deepLink){
		$(tl + '[href$="'+ deepLink +'"]').addClass("active");
	}else{
		$(tl[0]).addClass("active");
		//set hash, because it's undefined at the moment
		window.location.hash = $(tl[0]).attr("href");
	}
	$(deepLink || tc[0]).show();

	//check if hash changes on back and forward button click
	if ("onhashchange" in window) {  
       //historyfeature only supported for modern browsers
	   //use http://benalman.com/projects/jquery-hashchange-plugin/ if really needed for everyone
	   $("#info").html("Info: Historyfeature unterstützt! (Vor- und Zurückbutton)");  
    }  
    function locationHashChanged() {  
		//only needed for additional tabs, use tl.removeClass("active") instead if you don't need this
		$("#tabs li a").removeClass("active"); 
		//only needed for additional tabs, use tc.hide() instead if you don't need this
		$(".tabContent").hide(); 
		$(tl + '[href$="'+ window.location.hash +'"]').addClass("active");
		$(window.location.hash).show();
    }  
	window.onhashchange = locationHashChanged; 
	
	$("#tabs").delegate("li", "click", function(evt) {
		//only needed for additional tabs, use tl.removeClass("active") instead if you don't need this
		$("#tabs li a").removeClass("active"); 
		$(this).find("a").addClass("active"); 
		//only needed for additional tabs, use tc.hide() instead if you don't need this
		$(".tabContent").hide(); 
		var activeTab = $(this).find("a").attr("href"); 
		$(activeTab).show();
		//reset deeplink
		window.location.hash = activeTab;
		evt.preventDefault();
	});
	
});
//]]>