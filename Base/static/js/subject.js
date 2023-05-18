const regex = /\/works\/(\w+)/;
function handleClick(event){
    console.log(event.target)
    window.open(`/book/${event.target.closest('.book-content').getAttribute('book_id')}`, '_blank').focus();

}

$(document).ready(function() {
  $.ajax({
    url: `https://openlibrary.org/subjects/${subject}.json?offset=0&limit=50`,
    method: 'GET',
    success: function(data) {
      let bookCards = document.getElementsByClassName('book-content');
      for (let i = 0; i<50; i++){
          let parent = bookCards[i];
          parent.addEventListener('click', handleClick);
          parent.style.cursor = "pointer"
          let key = data['works'][i]["key"].match(regex)[1]
          parent.setAttribute("book_id", key)
          if (data['works'][i]['cover_id']){
              parent.querySelector('[role="img"]').src = `https://covers.openlibrary.org/b/id/${data['works'][i]['cover_id']}-M.jpg`
          } else {
              parent.querySelector('[role="img"]').src = emptyCover;
          }

          parent.querySelector('[role="title"]').innerText = data['works'][i]['title']
          let authors = "";
          for (let author in data['works'][i]['authors']){
            authors += data['works'][i]['authors'][author]["name"] + "\n";
          }
          parent.querySelector('[role="authors"]').innerHTML = authors
      }
    },
    error: function(xhr, status, error) {
      console.log('Error:', error);
    }
  });
});
let offset = 50;
let loading = false;
window.onscroll = function(ev) {
        if ((window.innerHeight + Math.round(window.scrollY)) >= document.body.offsetHeight && !loading) {
                console.log('load')
                loading = true
                $.ajax({
                    url: `https://openlibrary.org/subjects/${subject}.json?offset=${offset}&limit=50`,
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
                            child.classList.add("col-3", "col-3", "col-md-4", "col-lg-2");
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