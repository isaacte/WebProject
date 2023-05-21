// Return the names of the book's authors
const getAuthorsString = (book) => {
    authors = book.authors;
    var names = [];
    for (const i in authors) {
        names.push(authors[i]['name']);
    }

    // Convert list to sting
    if (authors.length == 0) {
        return "Anonymous";
    } else {
        var authorsString = `<a class="author-link link-secondary" href="../author/${authors[0].id}">${authors[0].name}</a>`;
        authors.shift();
        while (authors.length > 0) {
            authorsString += `, <a class="author-link link-secondary" href="../author/${authors[0].id}">${authors[0].name}</a>`;
            authors.shift();
        }
    }
    
    return authorsString;
}

// Load books of the main screen
const setUp = async() => {
    // book = await getBook();
    $.ajax({
        url: `./api/books/${openlibrary_key}`,
        type: "GET",
        success: function(book) {
            let thisBook = book;
            authorsField = document.getElementById("authors-field");
            var html = "";
                
            // Add info to HTML
            html = getAuthorsString(book);
            authorsField.innerHTML = html;
            
        },
        error: function(error) {
            console.log(error);
        }
    });
}
let readButton = document.getElementById("read-button");
let removeBookButton = document.getElementById("remove-book-button");

if (!added){
    // Add book in the user's list
    readButton.addEventListener('click', markAsRead);
}

function markAsRead()  {
    console.log(`./api/books/${openlibrary_key}`);
    if (!added) {
        $.ajax({
            url: `/save_book`,
            data: {'book_id': openlibrary_key, action: 'add'},
            type: "POST",
            beforeSend: function (xhr){
                xhr.setRequestHeader('X-CSRFToken', csrftoken);
            },
            success: function(response) {
                readButton.classList.remove("btn-primary");
                readButton.classList.add("btn-success");
                readButton.setAttribute('data-bs-toggle', 'modal');
                readButton.setAttribute('data-bs-target', '#read-button-backdrop');
                readButton.innerHTML = "Read";
                readButton.removeEventListener('click', markAsRead)
                added = true;
            },
            error: function(error) {
                console.log(`ERROR: ${error}`);
            }
        });
    }
}

// Remove book from the user's list
removeBookButton.addEventListener('click', () => {
    if (added) {
        $.ajax({
            url: `/save_book`,
            data: {'book_id': openlibrary_key, action: 'remove'},
            type: "POST",
            beforeSend: function (xhr){
                xhr.setRequestHeader('X-CSRFToken', csrftoken);
            },
            success: function(response) {
                readButton.classList.remove("btn-success");
                readButton.classList.add("btn-primary");
                readButton.removeAttribute('data-bs-toggle');
                readButton.removeAttribute('data-bs-target');
                readButton.innerHTML = "Mark as read";
                added = false;
                readButton.addEventListener('click', markAsRead);
            },
            error: function(error) {
                console.log(`ERROR: ${error}`);
            }
        });
    }
});
