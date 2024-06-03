from django.http import HttpResponse
from django.shortcuts import render

from django_app.models import Book

# Create your views here.

# Add Start 2024/06/02
def index(request):
# Add Start 2024/06/03
    books = Book.objects.all().order_by('book_id') # 値を取得
# Add End   2024/06/03
    test_dict = {'temp_str': "This is test String"}    # KEY='temp_str'、VALUE='This is test String' として、html呼び出し時などに渡せる。
    return render(request, '../templates/index.html', context=test_dict)    # [html_template] から呼び出し
# Add End   2024/06/02

# Add Start 2024/06/03
def detail(request):
    test_dict = {'temp_str': "This is test String"}    # KEY='temp_str'、VALUE='This is test String' として、html呼び出し時などに渡せる。
    return render(request, '../templates/detail.html', context=test_dict)    # [html_template] から呼び出し
# Add End   2024/06/03
