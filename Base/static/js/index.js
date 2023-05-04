const listBooks = async() => {
    try {
        const response = await fetch("./books");
        const data = await response.json();
        return(data);
    } catch (error) {
        console.log(error);
    }
}

const getBookCard(book) {
    return `<img src="../../static/images/loading_background.avif" class="card-img-top" alt="INSERTAR AQUÍ IMAGEN">
    <div class="card-body">
      <h5 class="card-title">${book["title"]}</h5>
      <p class="card-text">${book["summary"]}</p>
      <p class="card-text"><small class="text-body-secondary">Author's name</small></p>
    </div>`;
}

const setUp = async() => {
    books = await listBooks();
    firstBook = books["books"][0];
    console.log(firstBook);
    console.log(firstBook["title"]);
    var firstElement = document.getElementById("firstElement"); // src="../../../media/${firstBook["image"]}"
    card = getBookCard(firstBook)
    firstElement.innerHTML = getBookCard(firstBook);
}

window.addEventListener("load", async () => {
    await setUp();
});