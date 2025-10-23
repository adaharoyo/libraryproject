"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lib.views import index_view
from lib.views import book_view,add_book_view
from lib.views import bookcopy_view,add_bookcopy_view
from lib.views import borrowing_view,add_borrowing_view
from lib.views import librarian_view,add_librarian_view
from lib.views import library_view,add_library_view
from lib.views import student_view,add_student_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index_view, name="index_page"), 
    path('book/', book_view, name='book'),
    path('bookcopy/',bookcopy_view, name='bookcopy'),
    path('borrowing/',borrowing_view, name='borrowing'),
    path('librarian/',librarian_view, name='librarian'),
    path('student/',student_view,name='student'),
    path('library/',library_view,name='library'),
    path('add_student/',add_student_view,name="student_page"),
    path('add_library/',add_library_view,name="library_page"),
    path('add_librarian/',add_librarian_view,name="librarian_page"),
    path('add_borrowing/',add_borrowing_view,name="borrowing_page"),
    path('add_bookcopy/',add_bookcopy_view,name="bookcopy_page"),
    path('add_book/',add_book_view,name='book_page')
]
