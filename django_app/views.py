from django.shortcuts import get_object_or_404, redirect, render

from django_app.forms import BookForm
from django_app.models import Book

# Create your views here.

# Add Start 2024/06/02
def index(request):
# Add Start 2024/06/03
# Update Start 2024/06/06
#    books = Book.objects.all().order_by('book_id')
    books = Book.objects.select_related('author', 'genre').order_by('book_id')
# Update End   2024/06/06
# Add Start 2024/06/05

# Add End   2024/06/05
# Add End   2024/06/03
# Update Start 2024/06/05
#    return render(request, '../templates/index.html', {'books':books})
    return render(request, '../templates/main/index.html', {'books':books})
# Update End   2024/06/05

# Add Start 2024/06/03
def detail(request, id=id):
    book = get_object_or_404(Book, pk=id)
    return render(request, '../templates/main/detail.html', {'book':book})
# Add End   2024/06/03

# Add Start 2024/06/05
def edit(request, id=None):

    if id:
        book = get_object_or_404(Book, pk=id)
    else:
        book = Book()

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('django_app:index')
    else:
        form = BookForm(instance=book)

    return render(request, '../templates/main/edit.html', dict(form=form, id=id))

def delete(request, id):
    book = get_object_or_404(Book, pk=id)
    book.delete()
    return redirect('django_app:index')
# Add End   2024/06/05
