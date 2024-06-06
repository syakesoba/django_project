# Add File 2024/06/04
from django.forms import ModelForm

from django_app.models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
# Update Start 2024/06/06
#        fields = ('title', 'author_id', 'genre_id')
        fields = ('title', 'author', 'genre')
# Update End   2024/06/06