from django.shortcuts import render

from lib.forms import StudentForm,BookForm,BookcopyForm,LibrarianForm,LibraryForm,BorrowingForm

# Create your views here.
def index_view(request):
    return render (request,'index.html')

def book_view(request):
    return render(request,'book.html')

def bookcopy_view(request):
    return render(request,'bookcopy.html')

def borrowing_view(request):
    return render(request,'borrowing.html')

def librarian_view(request):
    return render(request,'librarian.html')

def student_view(request):
    return render(request,'student.html')

def library_view(request):
    return render(request,'library.html')



def add_student_view(request):
    message = ''
    if request.method =="POST":
        student_form = StudentForm(request.POST)

        if student_form.is_valid():
            student_form.save()
            message = "Student Added Successfully"

    else:
        student_form = StudentForm() 


    context = {
        'form': student_form,
        'message': message,
    } 

    return render(request,"add_student.html",context)          


def add_book_view(request):
    if request.method =="POST":
        book_form = BookForm(request.POST)

        if book_form.is_valid():
            book_form.save()

    else:
        book_form = BookForm() 


    context = {
        'form': book_form,
    } 

    return render(request,"add_book.html",context)  


def add_bookcopy_view(request):
    if request.method =="POST":
        bookcopy_form = BookcopyForm(request.POST)

        if bookcopy_form.is_valid():
            bookcopy_form.save()

    else:
        bookcopy_form = StudentForm() 


    context = {
        'form': bookcopy_form,
    } 

    return render(request,"add_bookcopy.html",context)  

def add_library_view(request):
    if request.method =="POST":
        library_form = LibraryForm(request.POST)

        if library_form.is_valid():
            library_form.save()

    else:
        library_form = LibraryForm() 


    context = {
        'form': library_form,
    } 

    return render(request,"add_library.html",context)          

def add_librarian_view(request):
    if request.method =="POST":
        librarian_form = LibrarianForm(request.POST)

        if librarian_form.is_valid():
            librarian_form.save()

    else:
        librarian_form = LibrarianForm() 


    context = {
        'form': librarian_form,
    } 

    return render(request,"add_librarian.html",context)   


def add_borrowing_view(request):
    if request.method =="POST":
        borrowing_form = BorrowingForm(request.POST)

        if borrowing_form.is_valid():
            borrowing_form.save()

    else:
        borrowing_form = BorrowingForm() 


    context = {
        'form': borrowing_form,
    } 

    return render(request,"add_borrowing.html",context)          



