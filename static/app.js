var map;
function initialize() {
  var mapOptions = {
    zoom: 16,
    center: new google.maps.LatLng(-27.500070, 153.014587)
  };
  map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);
}

google.maps.event.addDomListener(window, 'load', initialize);

var markers = [];
var line = [];

var displayData = function(data) {
	if (data == null)
		return;
	for (var i = 0; i < data.length; i++) {
		var pos = new google.maps.LatLng(data[i].latitude, data[i].longitude);
		var marker = new google.maps.Marker({
			position: pos,
			map: map,
			title: "Test",
			animation: google.maps.Animation.DROP
		});
		markers.push(marker);
		line.push(pos);
		console.log(data[i]);
	}
	var path = new google.maps.Polyline({
		path: line
	});
	path.setMap(map);
};

var init = function() {
	$.ajax({
		url: "/data/data.json",
		success: displayData
	});	
}


$(document).ready(function() {
	$('#display').click(function(e) {
		e.preventDefault();
		init();
	});
});