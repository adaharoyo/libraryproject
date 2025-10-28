from django.shortcuts import render, redirect

from lib.forms import StudentForm,BookForm,BookcopyForm,LibrarianForm,LibraryForm,BorrowingForm
from lib.models import Student,Librarian,Library,Book,Bookcopy,Borrowing
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

    students = Student.objects.all()
    
    context = {
        'form': student_form,
        'message': message,
        'students': students,
    } 

    return render(request,"add_student.html",context) 

def edit_student_view(request,student_id):
    message = ''
    student = Student.objects.get(id=student_id)

    if request.method == "POST":
        student_form = StudentForm(request.POST,instance=student)

        if student_form.is_valid():
            student_form.save()
            message = "changes saved successfuly"

        else:
            message = "Invalid!"

    else:
        student_form = StudentForm(request.POST,instance=student) 

    context = {
        'form' : student_form,
        'student' : student

    }    

    return render(request, 'edit_student.html',context)           
    

def delete_student_view(request,student_id):
    student =Student.objects.get(id=student_id)    


    student.delete()

    return redirect( add_student_view)





def add_book_view(request):
    message=''
    if request.method =="POST":
        book_form = BookForm(request.POST)

        if book_form.is_valid():
            book_form.save()
            message = "Added successfully"

    else:
        book_form = BookForm() 

    books = Book.objects.all()    


    context = {
        'form': book_form,
        'message':message,
        'books': books,
    } 

    return render(request,"add_book.html",context)  

def edit_book_view(request,book_id):
    message = ''
    book = Book.objects.get(id=book_id)

    if request.method == "POST":
        book_form = BookForm(request.POST,instance=book)

        if book_form.is_valid():
            book_form.save()
            message = "changes saved successfuly"

        else:
            message = "Invalid!"

    else:
        book_form = BookForm(request.POST,instance=book) 

    context = {
        'form' : book_form,
        'book' : book

    }    

    return render(request, 'edit_book.html',context)           
    

def delete_book_view(request,book_id):
    book =Book.objects.get(id=book_id)    


    book.delete()

    return redirect( add_book_view)





def add_bookcopy_view(request):
    message =''
    if request.method =="POST":
        bookcopy_form = BookcopyForm(request.POST)

        if bookcopy_form.is_valid():
            bookcopy_form.save()
            message="added successfully"

    else:
        bookcopy_form = BookcopyForm() 

    bookcopies=Bookcopy.objects.all()    


    context = {
        'form': bookcopy_form,
        'message':message,
        'bookcopies': bookcopies,
    } 

    return render(request,"add_bookcopy.html",context)

def edit_bookcopy_view(request,bookcopy_id):
    message = ''
    bookcopy = Bookcopy.objects.get(id=bookcopy_id)

    if request.method == "POST":
        bookcopy_form = BookcopyForm(request.POST,instance=bookcopy)

        if bookcopy_form.is_valid():
            bookcopy_form.save()
            message = "changes saved successfuly"

        else:
            message = "Invalid!"

    else:
        bookcopy_form = BookcopyForm(request.POST,instance=bookcopy) 

    context = {
        'form' : bookcopy_form,
        'bookcopy' : bookcopy

    }    

    return render(request, 'edit_bookcopy.html',context) 

def delete_bookcopy_view(request,bookcopy_id):
    bookcopy =Bookcopy.objects.get(id=bookcopy_id)    


    bookcopy.delete()

    return redirect( add_bookcopy_view)          
    


   


def add_library_view(request):
    message = ''
    if request.method =="POST":
        library_form = LibraryForm(request.POST)

        if library_form.is_valid():
            library_form.save()
            message="added succesfully"

    else:
        library_form = LibraryForm() 

    libraries=Library.objects.all()    


    context = {
        'form': library_form,
        'message': message,
        'libraries':libraries,
    } 

    return render(request,"add_library.html",context)  

 
def edit_library_view(request,library_id):
    message = ''
    library = Library.objects.get(id=library_id)

    if request.method == "POST":
        library_form = LibraryForm(request.POST,instance=library)

        if library_form.is_valid():
            library_form.save()
            message = "changes saved successfuly"

        else:
            message = "Invalid!"

    else:
        library_form = LibraryForm(request.POST,instance=library) 

    context = {
        'form' : library_form,
        'library' : library

    }    

    return render(request, 'edit_library.html',context)

def delete_library_view(request,library_id):
    library =library.objects.get(id=library_id)    


    library.delete()

    return redirect( add_library_view)           
    


       

def add_librarian_view(request):
    message=''
    if request.method =="POST":
        librarian_form = LibrarianForm(request.POST)

        if librarian_form.is_valid():
            librarian_form.save()
            message="added "

    else:
        librarian_form = LibrarianForm() 

    librarians=Librarian.objects.all()    


    context = {
        'form': librarian_form,
        'messsage':message,
        'librarians':librarians
    } 

    return render(request,"add_librarian.html",context) 

def edit_librarian_view(request,librarian_id):
    message = ''
    librarian = librarian.objects.get(id=librarian_id)

    if request.method == "POST":
        librarian_form = LibrarianForm(request.POST,instance=Librarian)

        if librarian_form.is_valid():
            librarian_form.save()
            message = "changes saved successfuly"

        else:
            message = "Invalid!"

    else:
        librarian_form = LibrarianForm(request.POST,instance=librarian) 

    context = {
        'form' : librarian_form,
        'librarian' : librarian

    }    

    return render(request, 'edit_librarian.html',context)


def delete_librarian_view(request,librarian_id):
    librarian =librarian.objects.get(id=librarian_id)    


    librarian.delete()

    return redirect( add_librarian_view)    
    






def add_borrowing_view(request):
    message=''
    if request.method =="POST":
        borrowing_form = BorrowingForm(request.POST)

        if borrowing_form.is_valid():
            borrowing_form.save()
            message="success"

    else:
        borrowing_form = BorrowingForm() 

    borrow=Borrowing.objects.all()

    context = {
        'form': borrowing_form,
        'message':message,
        'borrow':borrow,
    } 

    return render(request,"add_borrowing.html",context)          



