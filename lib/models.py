from django.db import models

# Create your models here.
class Book(models.Model):
    TYPE_OPTIONS=[
         ("F","Fiction"),
         ("NF","Non Fiction"),
         ("S","Science"),
         ("E","Encyclopedia"),
    ]
    title =models.CharField(max_length=60)
    publication_date=models.DateField(auto_now=False)
    author=models.CharField(max_length=60)
    type=models.CharField(max_length=4,choices=TYPE_OPTIONS)
    language=models.CharField(max_length=30)

    def  __str__(self):
        return  self.title

class Bookcopy(models.Model):
    STATUS_OPTIONS=[
        ("A","Available"),
        ("NA","Not Availabe"),
    ]
    book =models.ForeignKey(Book,on_delete=models.CASCADE)    
    status =models.CharField(max_length=4,choices=STATUS_OPTIONS)
    serial_number=models.CharField(max_length=20)

    def __str__(self):
                return f"{self.book.title} - SN: {self.serial_number}"


class Student(models.Model):
    GENDER_OPTIONS=[
        ("M","MALE"),
        ("F","FEMALE"),
    ]
    ENROLLMENT=[
        ("R","REGISTERED"),
        ("NA","NOT REGISTERED")
    ]
    YEAR_OPTIONS=[
         ("O","ONE"),
         ("T","TWO"),
         ("TH","THREE"),
         ("F","FOUR"),
    ]
    first_name=models.CharField(max_length=20)    
    last_name=models.CharField(max_length=20)
    course=models.CharField(max_length=10)
    year=models.CharField(max_length=4,choices=YEAR_OPTIONS)
    gender=models.CharField(max_length=2,choices=GENDER_OPTIONS)
    enrollment_status=models.CharField(max_length=4,choices=ENROLLMENT)

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"

class Borrowing(models.Model):
    borrow_date = models.DateField(auto_now=False)    
    bookcopy = models.ForeignKey(Bookcopy,on_delete=models.CASCADE)
    return_date = models.DateField(auto_now=False)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return f"Borrowed on {self.borrow_date} by {self.student}"


class Library(models.Model):
    name=models.CharField(max_length=20)
    location=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    GENDER_OPTIONS=[
        ("M","MALE"),
        ("F","FEMALE"),
    ]
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    gender =models.CharField(max_length=2,choices=GENDER_OPTIONS)
    contact =models.CharField(max_length=11)
    library=models.ForeignKey(Library,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    
