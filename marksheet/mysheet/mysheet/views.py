from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import *

def index(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('class1'):
            post=names()
            post.name= request.POST.get('name')
            post.class1= request.POST.get('class1')
            post.save()
            subjects = subject()
            subjects.Hindi = request.POST.get('Hindi')
            subjects.English = request.POST.get('English')
            subjects.Chemistry = request.POST.get('Chemistry')
            subjects.Maths = request.POST.get('Maths')
            subjects.physics = request.POST.get('physics')
            subjects.save()
            return render(request, 'index.html')  

    else:
        return render(request,'index.html')

  
    return render(request,"index.html")

# def demo(request):
#     student = stu_name.objects.get(hindi="hindi")
#     return render(request,"demo.html",{"student": student})


def demo(request):
    c = names.objects.all()

    return render(request, "demo.html", {'c': c})