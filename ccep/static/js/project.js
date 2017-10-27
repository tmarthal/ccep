/* Project specific Javascript goes here. */

/*
Formatting hack to get around crispy-forms unfortunate hardcoding
in helpers.FormHelper:

    if template_pack == 'bootstrap4':
        grid_colum_matcher = re.compile('\w*col-(xs|sm|md|lg|xl)-\d+\w*')
        using_grid_layout = (grid_colum_matcher.match(self.label_class) or
                             grid_colum_matcher.match(self.field_class))
        if using_grid_layout:
            items['using_grid_layout'] = True

Issues with the above approach:

1. Fragile: Assumes Bootstrap 4's API doesn't change (it does)
2. Unforgiving: Doesn't allow for any variation in template design
3. Really Unforgiving: No way to override this behavior
4. Undocumented: No mention in the documentation, or it's too hard for me to find
*/
$('.form-group').removeClass('row');



function selectCounty(countyId) {
  //todo don't hardcode the urls :(
  location.href = '/siting/'+countyId;
}

function selectModel(modelId) {
  var searchParams = new URLSearchParams(location.search)
  searchParams.set('sitingModelId', modelId);
  window.history.replaceState({}, '', location.pathname + '?' + searchParams);
}

// Add enter to trigger address lookup
$("#address").keydown(function(e) {
    var key = e.charCode ? e.charCode : e.keyCode ? e.keyCode : 0;
    if(key == 13) {
        $("#geolocate").click();
    }
});

// global variable :X
addressMarker = undefined;
function geoLookup() {
    var address = $("#address").val();

    console.log("looking up " + address)

    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

    // 397 N High St. Sacramento, CA 98021
    //'addr': '1601 E 3rd St, San Bernardino, CA 92408',
    var data = {
        'addr': address,
        csrfmiddlewaretoken: csrftoken
    }
    jQuery.post('/api/geocode', data, function(response) {
        console.log(response);
        //var map = L.map('map');
        if (response.lat && response.lon) {
            // center the map on the marker
            map.setView([response.lat, response.lon], 13);

//        L.marker(new L.LatLng(38.5826851, -121.4441873)).addTo(map)
//            .bindPopup('A pretty CSS3 popup.<br> Easily customizable.')
//        .openPopup();

            if (addressMarker) {
                map.removeLayer(addressMarker);
            }
            addressMarker = L.marker([response.lat, response.lon]).addTo(map)
            var searchParams = new URLSearchParams(location.search)
            searchParams.set('lat', response.lat);
            searchParams.set('lon', response.lon);
            window.history.replaceState({}, '', location.pathname + '?' + searchParams);
        }
        //setMessage(response.message)
    });
}

