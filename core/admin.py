from django.contrib import admin
from .models import Book, Publisher

# Register your models here.
admin.site.register(Book)
admin.site.register(Publisher)

# >>> ubs = Publisher.objects.annotate(num_books=Count('book')).order_by('-num_books')
# >>> ubs = Publisher.objects.annotate(num_books=Count('book')).order_by('-num_books')[1] 
# >>> ubs
# <Publisher: Publisher object (2)>
# >>>