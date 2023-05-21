$(function () {
  var selectedEditionKey; // Variable global para almacenar el edition key del libro seleccionado

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
        },
        success: function (data) {
          response($.map(data.docs.slice(0, 5), function (item) {
            return {
              label: item.title,
              editionKey: item.edition_key[0] // Guarda el edition key del libro en la propiedad "editionKey"
            }
          }));
        },
        error: function (error) {
          console.log(error);
        }
      });
    },
    select: function (event, ui) {
      redirectToBookPage(ui.item.editionKey);
    }
  });

  // Función para redirigir a la página del libro
  function redirectToBookPage(book_id) {
      window.location.href = '/book/' + book_id;
  }
});
