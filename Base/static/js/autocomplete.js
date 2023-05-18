
$(function () {
    
    $("#search-bar").autocomplete({
        
        source: function (request, response) {
            $.ajax({
                
                url: "https://openlibrary.org/search.json?title=" + request.term,
                dataType: "json",
                data: {
                    featureClass: "P",
                    type: "json",
                    maxRows: 5,
                    name_startsWith: request.term,
                    username: "admin"
                },
                
                
                success: function (data) {

                    response($.map(data.docs.slice(0,5), function (item) {

                        return {
                            label: item.title
                        }
                    }));
                },
                error: function(error) {

                    console.log(error);
                }
            });
        },
        minLength: 2,
        select: function (event, ui) {
            if (ui.item) {
                $("#id_stateOrProvince").val(ui.item.stateOrProvince);
                $("#id_country").val(ui.item.countryName);
                $("#id_zipCode").val("");
            }
        }
    });
});