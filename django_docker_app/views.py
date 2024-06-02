from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
# Add Start 2024/06/02
    test_dict = {'temp_str': "This is test String"}    # KEY='temp_str'、VALUE='This is test String' として、html呼び出し時などに渡せる。
    return render(request, '../templates/index.html', context=test_dict)    # [html_template] から呼び出し
# Add End   2024/06/02
