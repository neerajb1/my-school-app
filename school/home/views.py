from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html", {})

# def events(request):
#     return render(request , "events.html" , {})

def gallery(request):
    return render(request , "gallery.html" , {})

def course(request):
    return render(request , "course.html" , {})

def contact(request):
    return render(request , "contact.html" , {})

def student(request):
    return render(request , "Student.html" , {})

def teacher(request):
    return render(request , "teacher.html" , {})
