const regex = /\/works\/(\w+)/;
function handleClick(event){
    window.location.href = `/book/${event.target.closest('.book-content').getAttribute('book_id')}`;
}

window.onload = function(){load_books(); console.log('load')}

let cleanSubject = subject.replace(/ /g, '_').replace('&amp', '&').toLowerCase();
let offset = 0;
let loading = false;
window.onscroll = function (ev){load_books(ev)}

    function load_books (ev) {
        if ((window.innerHeight + Math.round(window.scrollY)) + 100 >= document.body.offsetHeight && !loading) {
                console.log('load')
                loading = true
                $.ajax({
                    url: `https://openlibrary.org/subjects/${cleanSubject}.json?offset=${offset}&limit=50`,
                    method: 'GET',
                    success: function (data) {
                        let parent = document.getElementById('books-container');
                        for (let book in data["works"]) {
                            let authors = "";
                            for (let author in book['authors']) {
                                authors += data['works'][book]['authors'][author]["name"] + "\n";
                            }
                            let cover;
                            if (data['works'][book]["cover_id"]){
                                cover = `https://covers.openlibrary.org/b/id/${data['works'][book]["cover_id"]}-M.jpg`;
                            } else {
                                cover = emptyCover;
                            }
                            let child = document.createElement("div");
                            let key = data['works'][book]["key"].match(regex)[1];
                            child.classList.add("col-sm-6", "col-md-4", "col-lg-2");
                            child.innerHTML = `
                            <div class="card mb-3 book-content" aria-hidden="true" book_id="${key}">
                                <img src="${cover}" role="img" class="card-img-top">
                                <div class="card-body">
                                  <h5 class="card-title placeholder-glow" role="title">${data['works'][book]["title"]}</h5>
                                  <p class="card-text placeholder-glow" role="authors">${authors}</p>
                                </div>
                            </div>
                            `
                            parent.appendChild(child);
                            child.addEventListener('click', handleClick);
                            child.style.cursor = "pointer"
                        }
                        offset += 50;
                        if (offset >= data["work_count"]){
                            window.onscroll = null;
                        }
                    },
                    error: function (xhr, status, error) {
                        console.log('Error:', error);
                    }
                });
                loading = false;
            }
};