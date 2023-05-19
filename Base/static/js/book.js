// Return a list of books from a json object. Return null if there aren't any book.
const getBook = async() => {
    // try {
    //     const response = await fetch(`../api/books/${openlibrary_key}`);
    //     const data = await response.json();
    //     return data;
    // } catch (error) {
    //     console.log(error);
    // }
}

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

window.addEventListener("load", async () => {
    console.log(`${book}`);
    await setUp();
});

readButton = document.getElementById("read-button");
removeBookButton = document.getElementById("remove-book-button");

added = false;

const addBook = async(book_id) => {
    const response = await fetch(url, {
        method: 'PUT',
        headers: {
          'Content-type': '../api/'
        },
        body: JSON.stringify(book_id)
      });
}

// Add book in the user's list
readButton.addEventListener('click', async() => {
    console.log(`./api/books/${openlibrary_key}`);
    if (!added) {
        $.ajax({
            url: `../../api/books/${openlibrary_key}`,
            type: "GET",
            success: function(book) {
                console.log(book);
                addBook(openlibrary_key);
            },
            error: function(error) {
                console.log(error);
            }
        });
        
        readButton.classList.remove("btn-primary");
        readButton.classList.add("btn-success");
        readButton.setAttribute('data-bs-toggle', 'modal');
        readButton.setAttribute('data-bs-target', '#read-button-backdrop');
        readButton.innerHTML = "Read";
        added = true;
    }
});

// Remove book from the user's list
removeBookButton.addEventListener('click', () => {
    if (added) {
        readButton.classList.remove("btn-success");
        readButton.classList.add("btn-primary");
        readButton.removeAttribute('data-bs-toggle');
        readButton.removeAttribute('data-bs-target');
        readButton.innerHTML = "Mark as read";
        added = false;
    }
});
