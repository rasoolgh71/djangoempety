from django.shortcuts import render,HttpResponse
from datetime import datetime
import time
import pytz
from .forms import Emailform
# Create your views here.

def home(request):
    tz=pytz.timezone('Asia/Tehran')
    date=datetime.now(tz=tz)
    date=date.isoformat()
    #html = "<html><body>It is now %s.</body></html>" % date
    #return HttpResponse(html)
    #date=time.strftime("%Y-%m-%D %H:%M:%S")
    name="RASOOL"


    return render(request, 'task/home.html', context = {'date':date,'name':name})
    #return HttpResponse('hello')

def show(request):
    form = Emailform(request.POST)

    # if request.method == "POST":
    #     form = Emailform(request.POST)
    #     #if form.is_valid():
    #     subject = form.cleaned_data['subject']
    #     email = form.cleaned_data['email']
    #     message = form.cleaned_data['message']
    #     number = form.cleaned_data['number']
    return render(request,'task/show.html',context={'form':form})

def testjave(request):
    return  render(request,'task/testjava.html')

def sendemail(request):
    form=Emailform(request.POST)
    if form.is_valid():
        subject = request.POST.get('subject', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        number = request.POST.get('number', '')

    return render(request,'task/email.html',context={'form':form})