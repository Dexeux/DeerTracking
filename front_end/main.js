function getRandomInRange(from, to, fixed) {
    return (Math.random() * (to - from) + from).toFixed(fixed) * 1;
    // .toFixed() returns string, so ' * 1' is a trick to convert to number
}
var map;
var flightPath;
var animalColors = [];
var flightPaths = [];
var overflowFlightpaths = [];
var currentAnimal;
var firstDate;
var endDate;

function loadBinaryFile(path, success) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", path, true);
    xhr.responseType = "arraybuffer";
    xhr.onload = function() {
        var data = new Uint8Array(xhr.response);
        var arr = new Array();
        for (var i = 0; i != data.length; ++i) arr[i] = String.fromCharCode(data[i]);
        success(arr.join(""));
    };
    xhr.send();
};




function initMap() {
    map = new google.maps.Map(document.getElementById('content'), {
        center: flightPaths[flightPaths.length - 1],
        zoom: 4,
        mapTypeControlOptions: {
            position: google.maps.ControlPosition.RIGHT_BOTTOM,
            style: google.maps.MapTypeControlStyle.DEFAULT
        },
        streetViewControl: false,
        zoomControlOptions: {
            style: google.maps.MapTypeControlStyle.DEFAULT,
            position: google.maps.ControlPosition.RIGHT_BOTTOM
        }
    });


    flightPath = new google.maps.Polyline({
        path: flightPaths,
        geodesic: true,
        strokeColor: animalColors[currentAnimal],
        strokeOpacity: 1.0,
        strokeWeight: 2
    });
    flightPath.setMap(map);


    var gooseMarker = 'goose.png';
    var beachMarker = new google.maps.Marker({
        position: flightPaths[flightPaths.length - 1],
        map: map,
        icon: gooseMarker
    });
}





$(document).ready(function() {
    $(document).keypress(function(e) {
  if(e.which == 49) {
    overflowFlightpaths[overflowFlightpaths.length] = flightPaths.pop();
    initMap();
  }
  if(e.which == 50){
    flightPaths.push(overflowFlightpaths.pop());
    initMap();
  }
});

    loadBinaryFile('./migrations.db', function(data) {
        var sqldb = new SQL.Database(data);
        // Database is ready
        var res = sqldb.exec("SELECT * FROM raw_data WHERE individual_local_identifier='72413'");

        var raw_data = jQuery.parseJSON(JSON.stringify(res))[0].values;
        var length_of_data = raw_data.length;
        firstDate = raw_data[0][1];
        lastDate = raw_data[raw_data.length - 1][1];

        for (i = 0; i < length_of_data; i++) {
            flightPaths[i] = { lat: raw_data[i][2], lng: raw_data[i][3] };
        }
        initMap();
    });

    document.getElementById('color-selector-value').value = animalColors[0];
    updateTextInput = function(val) {
        document.getElementById('animal-selector-value').innerHTML = 'Options for Goose #' + val;
        currentAnimal = val;
        document.getElementById('color-selector-value').value = animalColors[currentAnimal] ? animalColors[currentAnimal] : '';

    }

    changedColorAnimal = function(val) {
        document.getElementById('color-selector-value').value = val;
        animalColors[currentAnimal] = '#' + val;
        flightPath.strokeColor = '#' + val;
        initMap();

    }
    var startDate = 0;
    var endDate = 0;

    var hideTime = function() {
        $('.menu-control').removeClass('fa-caret-left').addClass('fa-caret-right');
        $('.time-control').addClass('hidden');
        $('#startDate, #endDate, .to').addClass('hide');
    }
    var showTimePartial = function() {
        $('#startDate, #endDate, .to').removeClass('hide');
    }

    var showTime = function() {
        $('.menu-control').removeClass('fa-caret-right').addClass('fa-caret-left');
        $('.time-control').removeClass('hidden');
        setTimeout(showTimePartial, 1000);

    }
    $('.menu-control').click(function(event) {
        $('.time-control').hasClass('hidden') ? showTime() : hideTime();
    });

    var startPicker = new Pikaday({
        field: $('#startDate')[0],
        onSelect: function() {
            startDate = this.getMoment().format('Do MMMM YYYY');
            $('.startSmallDate').text(startDate);
        }
    });
    var endPicker = new Pikaday({
        field: $('#endDate')[0],
        onSelect: function() {
            endDate = this.getMoment().format('Do MMMM YYYY');
            $('.startEndDate').text(endDate);

        }
    });
});
