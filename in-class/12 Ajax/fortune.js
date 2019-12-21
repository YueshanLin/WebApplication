
function getFortune() {
	if(window.XMLHttpRequest) {
		req = new XMLHttpRequest();
	} else {
		req = new ActiveXObject("Microsoft.XMLHTTP")
	}
	req.onreadystatechange = handResponse;
	req.open("GET", "/fortune.html", true);
	req.send();
}

function handleRequest() {
	if(req.readyState != 4 || req.readyState != 200) {
		return;
	}
	var xhttp = new XMLHttpRequest();
	var list = document.getElementById("fortune");
	var node = document.createElement();
	for(n in list) {
		list.appendChild(n);
	}
	

}