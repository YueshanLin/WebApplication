/*
function addFunction() {
  		var node = document.createElement("LI");

  		var textnode = document.createTextNode(document.getElementById("textfield").value);
  		node.appendChild(textnode);
  		document.getElementById("todolist").appendChild(node);
}
*/

function addFunction(parentID, elementTag, elementID, html) {
	var parent = document.getElementById(parentID);
	//var newElement = document.createTextNode(document.getElementById("textfield").value);
	var newElement = document.createElement(elementTag);
	var textNode = document.createTextNode(document.getElementById("textfield").value);
	newElement.appendChild(textNode);
	newElement.setAttribute('id', elementID);
	newElement.innerHTML = html;
	parent.appendChild(newElement.value);
}

function deleteFunction(elementID) {
	var element = document.getElementById(elementID);
	element.parent.removeChild(element);
}


var fieldID = 0;
function add() {
	fieldID ++;
	var html = '<input type="text" name="item"> <a href="" onclick="javascript:deleteFunction( fieldID);"> Delete</a>';
	addFunction('todolist', 'li', fieldID, html);
}