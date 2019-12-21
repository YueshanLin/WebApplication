function initialize() {
	document.getElementById("timestamp").value = 0.0;
}

function update() {
	var list = $("#posts");
	var timestamp = document.getElementById("timestamp").value;
	//var timestamp = 0;
	console.log("before update-----------------------------");
	console.log(timestamp);
	$.get("get_changes?time=" + timestamp)
	.done(function(data) {
		// Update the most recent time
		document.getElementById("timestamp").value = data['timestamp'];
		console.log("AFTER update-----------------------------");
		console.log(data['timestamp']);


		list.data("timestamp", data['timestamp']);

		// Inserting posts
		for(var i = 0; i < data.posts.length; i ++) {
			var post = data.posts[i];
			
			var parser = new DOMParser;
			var dom = parser.parseFromString(post.html,"text/html");
			var newPost = $.parseHTML(dom.body.textContent);

			//var newPost = $(post.html);
			/*
			newPost.data("user", post.user);
			newPost.data("time", post.time);
			newPost.data("comment", post.comment);
			*/
			list.prepend(newPost);
			$("#submit_" + post.id).click(addSubPost);
		}

		for(var i = 0; i < data.subPosts.length; i ++) {
			var subPost = data.subPosts[i];

			var parser = new DOMParser;
			var dom = parser.parseFromString(subPost.html,"text/html");
			var newSubPost = $.parseHTML(dom.body.textContent);

			$("#subPost_" + subPost.post_id).append(newSubPost);
		}

		

	});
}

function addPost(event) {
	event.preventDefault();
	var comment = $("#writePost").val();
	$.post("add_post", {"comment": comment})
	.done(function(data) {
		
		update();
		$("#writePost").val("").focus();
		document.getElementById("timestamp").value = data['timestamp'];
		
	});
}


function addSubPost(event) {
	
	event.preventDefault();

	var post_id = parseInt($(this).attr("id").substring(7), 10);

	var comment = $("#writeSubPost_" + post_id).val();
		
	$.post('add_subPost/' + post_id, {"comment": comment})
	.done(function(data) {
		
		update();
		$("#writeSubPost_" + post_id).val("").focus();
		document.getElementById("timestamp").value = data['timestamp'];
		/*
		// Inserting the data into html format
		newSubPost = $(data.html);
		$("#subPost_" + post_id).append(newSubPost);
		*/
	});
}


$(document).ready(function(){

	initialize();

	$('#submitPost').click(addPost);
  	//populatePost();
  	update();
	window.setInterval(update, 5000);

	// CSRF set-up copied from Django docs

	function getCookie(name) {  
    	var cookieValue = null;
    	if (document.cookie && document.cookie != '') {
        	var cookies = document.cookie.split(';');
        	for (var i = 0; i < cookies.length; i++) {
            	var cookie = jQuery.trim(cookies[i]);
            	// Does this cookie string begin with the name we want?
            	if (cookie.substring(0, name.length + 1) == (name + '=')) {
                	cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                	break;
            	}
        	}
    	}
    	return cookieValue;
  	}
	var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
	    beforeSend: function(xhr, settings) {
	    	xhr.setRequestHeader("X-CSRFToken", csrftoken);
		}
	});
});



// Useful for debugging
/*
	$.ajax ({
	    url: "get_changes",
	    dataType: 'json',
	    data: { areaID: $("#lbxArea").val () },
	    success: function (data) {
	        // Use data for actions
	    },
	    error: function (jqXHR, textStatus, errorThrown) {
	        console.log(textStatus);
	        console.log(errorThrown);
	    }
	});
*/