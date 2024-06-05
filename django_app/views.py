from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from django_app.forms import BookForm
from django_app.models import Book

# Create your views here.

# Add Start 2024/06/02
def index(request):
# Add Start 2024/06/03
    books = Book.objects.all().order_by('book_id') # 値を取得
# Add End   2024/06/03
    return render(request, '../templates/index.html', {'books':books})
# Add End   2024/06/02

# Add Start 2024/06/03
def detail(request):
    test_dict = {'temp_str': "This is test String"}    # KEY='temp_str'、VALUE='This is test String' として、html呼び出し時などに渡せる。
    return render(request, '../templates/detail.html', context=test_dict)    # [html_template] から呼び出し
# Add End   2024/06/03

# Add Start 2024/06/05
def edit(request, id=None):

    if id:
        member = get_object_or_404(Book, pk=id)
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

    return render(request, 'book/edit.html', dict(form=form, id=id))

def delete(request, id):
    book = get_object_or_404(Book, pk=id)
    book.delete()
    return redirect('django_app:index')
# Add End   2024/06/05
