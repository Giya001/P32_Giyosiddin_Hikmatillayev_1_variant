from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from book import form
from book.form import BookForm
from book.models import Book


@login_required
# Create your views here.
def home(request):
    books = Book.objects.filter(is_read=True,user=request.user)
    search_book = request.GET.get('q')
    if search_book:
        books = Book.objects.filter(Q(title__icontains=search_book) | Q(author__icontains=search_book), is_read=True)

    return render(request, 'book/home.html', {'books': books})


@login_required
def home_not_read(request):
    books = Book.objects.filter(is_read=False)
    search_book = request.GET.get('q')
    if search_book:
        books = Book.objects.filter(Q(title__icontains=search_book) | Q(author__icontains=search_book), is_read=True)

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


def update(request, book_id):
    book = get_object_or_404(Book, id=book_id, author=request.user)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save()
            if book.is_read:
                return redirect('home')
            return redirect('home_not_read')
    else:
        form = BookForm(instance=book)
    return render(request, 'book/update.html', {'form': form, 'book': book})


def delete(request, book_id):
    book = get_object_or_404(Book, id=book_id, author=request.user)
    book.delete()
    return redirect('home')
