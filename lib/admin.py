from django.contrib import admin

from .models import Book
from .models import Bookcopy
from .models import Student
from .models import Borrowing
from .models import Librarian
from .models import Library

class StudentAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","year")

class LibraryAdmin(admin.ModelAdmin):
    list_display=("name","location")  

class LibrarianAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","gender","contact")   

class BorrowingAdmin(admin.ModelAdmin):
    list_display=("borrow_date","student")

class BookcopyAdmin(admin.ModelAdmin):
    list_display=("book","status") 

class BookAdmin(admin.ModelAdmin):
    list_display=("title","author")              

admin.site.register(Book,BookAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Library,LibraryAdmin)
admin.site.register(Librarian,LibrarianAdmin)
admin.site.register(Borrowing,BorrowingAdmin)
admin.site.register(Bookcopy,BookcopyAdmin)


