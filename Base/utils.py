import requests
from .models import Book, Author, AuthorInBook, LiteraryGenre, LiteraryGenreInBook
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO
from datetime import datetime
import re

def get_book(openlibrary_key):
    if Book.objects.filter(openlibrary_key=openlibrary_key).exists():
        return Book.objects.get(openlibrary_key=openlibrary_key)
    result = requests.get(f'https://openlibrary.org/works/{openlibrary_key}.json')
    if result.status_code != 200:
        return None
    result = result.json()
    b = Book(openlibrary_key = openlibrary_key,
                               title = result['title'])
    if 'description' in result:
        if 'value' in result['description']:
            b.summary = result['description']['value']
        else:
            b.summary = result['description']
    if 'covers' in result:
        b.image = f'https://covers.openlibrary.org/b/id/{result["covers"][0]}-L.jpg'
    b.save()
    if 'authors' in result:
        for author in result['authors']:
            if "author" in author:
                author = author["author"]
            key = re.search(r"/authors/(\w+)", author["key"]).group(1)
            a = get_author(key)
            AuthorInBook.objects.create(book=b, author=a)
    if 'subjects' in result:
        for genre in result['subjects']:
            genre_obj, created = LiteraryGenre.objects.get_or_create(name=genre)
            LiteraryGenreInBook.objects.create(literary_genre=genre_obj, book=b)
    return b

def get_author(openlibrary_key):
    if Author.objects.filter(openlibrary_key=openlibrary_key).exists():
        return Author.objects.get(openlibrary_key=openlibrary_key)
    result = requests.get(f'https://openlibrary.org/authors/{openlibrary_key}.json')
    if result.status_code != 200:
        return False
    result = result.json()
    a = Author(openlibrary_key=openlibrary_key,
               name=result['name'])
    image_req = requests.get(f'https://covers.openlibrary.org/a/olid/{openlibrary_key}-L.jpg')
    image = Image.open(BytesIO(image_req.content))
    width, height = image.size
    num_pixels = width * height
    if num_pixels > 1:
        a.image = f'https://covers.openlibrary.org/a/olid/{openlibrary_key}-L.jpg'
    if 'bio' in result:
        a.biography = result['bio']
    if 'birth_date' in result:
        try:
            a.birth_date = datetime.strptime(result['birth_date'], "%d %B %Y")
        except ValueError:
            pass
    if 'death_date' in result:
        try:
            a.decease_date = datetime.strptime(result['death_date'], "%d %B %Y")
        except ValueError:
            pass
    a.save()

    return a