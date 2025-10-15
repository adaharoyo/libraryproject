from django.shortcuts import render

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
