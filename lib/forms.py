from django.forms import ModelForm
from lib.models import Student,Librarian,Library,Book,Bookcopy,Borrowing



class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class LibrarianForm(ModelForm):
    class Meta:
        model=Librarian
        fields = '__all__'

class LibraryForm(ModelForm):
    class Meta:
        model=Library
        fields= '__all__'

class BookForm(ModelForm):
    class Meta:
        model=Book
        fields= '__all__'

class BookcopyForm(ModelForm):
    class Meta:
        model=Bookcopy
        fields= '__all__'      

class BorrowingForm(ModelForm):
    class Meta:
        model=Borrowing
        fields= '__all__'
