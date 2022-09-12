from calendar import c
from django.contrib import admin
from .models import Student, Feed

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']

@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = ['upload']