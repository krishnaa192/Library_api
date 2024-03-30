from django.contrib import admin

# Register your models here.
from .models import CustomUser, Book, Order, Category

admin.site.register(CustomUser)
admin.site.register(Book)
admin.site.register(Order)
admin.site.register(Category)
