
from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'cover_image_display')

    def cover_image_display(self, obj):
        if obj.cover_image:
            return f'<img src="{obj.cover_image.url}" width="50" height="70" style="object-fit: cover;" />'
        return "No Image"

    cover_image_display.allow_tags = True
    cover_image_display.short_description = 'Cover Image'