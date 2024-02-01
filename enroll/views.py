from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
# Create your views here.

# This function add and show your data
def add_show(request):
    if(request.method=='POST'):
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            # fm.save()  ##(it directly save all data) or,
            # it save data one by one
            
            nm=fm.cleaned_data["name"]
            em=fm.cleaned_data["email"]
            pw=fm.cleaned_data["password"]
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            fm=StudentRegistration()
    else:
        fm=StudentRegistration()
    
    stud=User.objects.all()
         
    return render(request, 'enroll/addAndShow.html',{'form':fm,'stu':stud,})