from django.contrib import admin

# Register your models here.

from .models import Category, Subject, Content

admin.site.register(Category)
admin.site.register(Subject)
admin.site.register(Content)