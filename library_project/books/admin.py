from django.contrib import admin



# Register your models here.
from books.models import Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author')
    search_fields = ('title',)
    list_filter = ('author',)
admin.site.register(Book,BookAdmin)
