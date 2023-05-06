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

// Return the authors of a book
const getAuthorsName = (book) => {
    authors = book.authors;
    var names = [];
    for (const i in authors) {
        names.push(authors[i]['name']);
    }
    return names;
}

// Return the html of a book card from a book object
const getBookCard = (book, authors) => {
    return `<div class="col-3 col-sm-6 col-md-4 col-lg-3">
        <div class="card mb-3">
           <img src="${book["image"]}" class="card-img-top" alt="INSERTAR AQUÍ IMAGEN">
           <div class="card-body">
                <h5 class="card-title">${book["title"]}</h5>
                <p class="card-text">${book["summary"]}</p>
                <p class="card-text"><small class="text-body-secondary">${authors}</small></p>
           </div>
        </div>
    </div>`;
}

// Load books of the main screen
const setUp = async() => {
    books = await listBooks();
    if (books == null) {
        console.log("There aren't books");
    } else {
        bestRatedBooks = document.getElementById("best-rated-books");
        var html = "";
        
        for (const i in books) {
            // Build author's format
            var authors = getAuthorsName(books[i]);
            var authorsString = `${authors[0]}`;
            console.log(authors);
            authors.shift();
            while(authors.length > 0) {
                authorsString += `, ${authors[0]}`;
                authors.shift();
            }

            // Add info to HTML
            html += getBookCard(books[i], authorsString);
        }
        bestRatedBooks.innerHTML = html;
    }
}

window.addEventListener("load", async () => {
    await setUp();
});