from django.contrib import admin

# Register your models here.
from .models import comment

@admin.register(comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'created_at')
