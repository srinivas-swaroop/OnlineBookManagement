from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books_pdfs/')
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)  # Added ImageField
    
    def __str__(self):
        return self.title
