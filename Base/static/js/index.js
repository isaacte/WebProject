// Constants declaration
MAX_WRITERS_SHOWED = 2;

// Return a list of books from a json object. Return null if there aren't any book.
const listBooks = async() => {
    try {
        const response = await fetch("./api/books");
        const data = await response.json();
        if (data.length == 0) {
            return null;
        } else {
            return data;
        }
    } catch (error) {
        console.log(error);
    }
}

// Return the names of the book's authors
const getAuthorsString = (book, maxAuthors = -1) => {
    authors = book.authors;

    // Convert list to sting
    authorsAdded = 0;
    if (authors.length == 0) {
        return "Anonymous";
    } else {
        var authorsString = `<a class="author-link link-secondary" href="author/${authors[0].id}">${authors[0].name}</a>`;
        authorsAdded++;
        authors.shift();
        while (authors.length > 0 && (maxAuthors == -1 || authorsAdded < maxAuthors)) {
            authorsString += `, <a class="author-link link-secondary" href="author/${authors[0].id}">${authors[0].name}</a>`;
            authorsAdded++;
            authors.shift();
        }

        if (authors.length > 0) {
            authorsString += ' and others';
        }
    }
    
    return authorsString;
}

// Return the html of a book card from a book object
const getBookCard = (book, authors) => {
    return `<div class="col-sm-6 col-md-4 col-lg-2">
    <a class="book-card link-underline link-underline-opacity-0 text-dark" href="./book/${book["ISBN"]}">
        <div class="card mb-3">
           <img src="${book["image"]}" class="card-img-top" alt="Book cover of '${book["title"]}'">
           <div class="card-body">
                <h5 class="card-title">${book["title"]}</h5>
                <p class="card-text">${book["summary"]}</p>
                <p class="card-text"><small class="text-body-secondary">${authors}</small></p>
           </div>
        </div>
    </a>
    </div>`;
}

// Load books of the main screen
const setUp = async() => {
    books = await listBooks();
    if (books == null) {
        console.log("There aren't books");
    } else {
        var bestRatedBooks = document.getElementById("best-rated-books");
        var html = "";
        
        // Add info to HTML
        for (const i in books) {
            var authors = getAuthorsString(books[i], MAX_WRITERS_SHOWED);
            html += getBookCard(books[i], authors);
        }
        bestRatedBooks.innerHTML = html;
    }
}

window.addEventListener("load", async () => {
    await setUp();
});