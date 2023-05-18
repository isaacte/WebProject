
$(function () {
    
    $("#search-bar").autocomplete({
        
        source: function (request, response) {
            $.ajax({
                
                url: "https://openlibrary.org/search.json?title=harry",
                dataType: "json",
                data: {
                    featureClass: "P",
                    type: "json",
                    maxRows: 5,
                    name_startsWith: request.term,
                    username: "admin"
                },
                
                
                success: function (data) {
                    console.log("hola");
                    response($.map(data.docs, function (item) {
                        console.log("hola2");
                        return {
                            label: item.title
                        }
                    }));
                },
                error: function(error) {
                    console.log("adeu");
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