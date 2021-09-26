from django.contrib import admin
from .models import Category, Book, Comment


class CommentInline(admin.TabularInline):
    model = Comment


class BookAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(Book, BookAdmin)
admin.site.register(Category)
admin.site.register(Comment)
