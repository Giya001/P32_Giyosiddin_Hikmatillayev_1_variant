from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from book import form
from book.form import BookForm
from book.models import Book


# Create your views here.
def home(request):
    books = Book.objects.all()
    search_book = request.GET.get('search_book')
    if search_book:
        books = books.objects.filter(Q(title__icontains=search_book) | Q(author__icontains=search_book), is_read=True)

    return render(request, 'book/home.html', {'books': books})


def createBook(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            if blog.is_read:
                return redirect('home')
            return redirect('home')
    else:
        form = BookForm()
    context = {
        'form': form
    }

    return render(request, 'book/create.html', context=context)


def updateBook(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            if book.is_read:
                return redirect('home')
            return redirect('home')

        else:
            form = BookForm(instance=book)

    context = {
        'book': book,
    }

    return render(request, 'book/update.html', context=context)
