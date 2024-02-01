from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.
def add_show(request):
    if(request.method=='POST'):
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=StudentRegistration()
         
    return render(request, 'enroll/addAndShow.html',{'form':fm})