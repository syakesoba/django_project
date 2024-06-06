from django.db import models

# Create your models here.

# Add Start 2024/06/03
# Manage author information
class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    author = models.CharField()
    add_datetime = models.DateTimeField()
    update_datetime = models.DateTimeField()
    delete_datetime = models.DateTimeField(null=True)

    def __str__(self):
        return self.author

# Manage genre information
class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    genre = models.CharField()
    add_datetime = models.DateTimeField()
    update_datetime = models.DateTimeField()
    delete_datetime = models.DateTimeField(null=True)

    def __str__(self):
        return self.genre

# Manage book information
class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
# Update Start 2024/06/06
#    author_id = models.IntegerField()
#    genre_id = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
# Update End   2024/06/06
    title = models.CharField()
    add_datetime = models.DateTimeField()
    update_datetime = models.DateTimeField()
    delete_datetime = models.DateTimeField(null=True)

    def __str__(self):
        return self.title
# Add End 2024/06/03