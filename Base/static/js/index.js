// Return a list of books from a json object. Return null if there aren't any book.
const listBooks = async() => {
    try {
        const response = await fetch("./books");
        const data = await response.json();
        if (data["message"] == "success") {
            return data["books"];
        } else {
            return null;
        }
    } catch (error) {
        console.log(error);
    }
}

// Return the html of a book card from a book object
const getBookCard = (book) => {
    return `<div class="col-3 col-sm-6 col-md-4 col-lg-3">
        <div class="card mb-3">
           <img src="../../static/images/loading_background.avif" class="card-img-top" alt="INSERTAR AQUÍ IMAGEN">
           <div class="card-body">
                <h5 class="card-title">${book["title"]}</h5>
                <p class="card-text">${book["summary"]}</p>
                <p class="card-text"><small class="text-body-secondary">Author's name</small></p>
           </div>
        </div>
    </div>`;
}

// Load books of the main screen
const setUp = async() => {
    books = await listBooks();
    console.log(books);
    if (books == null) {
        console.log("There aren't books");
    } else {
        firstBook = books[0];
        bestRatedBooks = document.getElementById("best-rated-books");
        var html = "";
        for (const i in books) {
            html += getBookCard(books[i]);
        }
        bestRatedBooks.innerHTML = html;
    }
}

window.addEventListener("load", async () => {
    await setUp();
});