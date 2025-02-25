from django.shortcuts import render
from admin_panel.models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'user_interface/book_list.html', {'books': books})



def home(request):
    return render(request, 'user_interface/admin_dashboard.html')

