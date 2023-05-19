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
            username: "admin"
          },
          success: function (data) {
            response($.map(data.docs.slice(0, 5), function (item) {
              return {
                label: item.title,
                editionKey: item.edition_key[0] // Guarda el edition key del libro en la propiedad "editionKey"
              }
            }));
  
            // Evento de selección del libro
            $("#search-bar").on("autocompleteselect", function (event, ui) {
              selectedEditionKey = ui.item.editionKey; // Almacena el edition key del libro seleccionado en la variable global
              console.log(selectedEditionKey); // Imprime el edition key del libro seleccionado en la consola
            });
          },
          error: function (error) {
            console.log(error);
          }
        });
      },
    });
  
    document.addEventListener('keydown', function (event) {
      if (event.key === 'Enter') {
        if (selectedEditionKey) {
          // Redirige a la URL con el edition key del libro seleccionado
          window.location.href = 'http://127.0.0.1:8000/book/' + selectedEditionKey;
        } else {
          // Si no se ha seleccionado ningún libro, redirige a la página principal
          window.location.href = 'http://127.0.0.1:8000';
        }
      }
    });
  });
  