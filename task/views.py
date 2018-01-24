from django.shortcuts import render,HttpResponse
import subprocess
from datetime import datetime
import time
import pytz
from .forms import Emailform
import re
from .models import Used
from .tasks import repeat_cheak_info
#from persion import print_hello
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

def csscode(request):
    return render(request,'task/csscode.html')

    return render(request,'task/show.html',context={'form':form})

def testjave(request):
    return render(request,'task/testjava.html')

def chartshow(request):
    data = {}
    process = subprocess.Popen(["df   |  awk  '{ print $1,$2, $3, $4 , $5 }'"],stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    disk, err = process.communicate()
    disk = disk.decode('utf-8').split('\n')
    print(disk)


    for i in disk:
        data[i] = i.split()
        #if(data[i]=='*G')

        #print(data[i])
        if(data[i]== ['Filesystem', '1K-blocks', 'Used', 'Available', 'Use%']):
            #data[i]=""
            del data[i]

    lister = []
    file = []
    size = []
    used = []
    avial = []

    for ii in disk:
        list = ii.split(" ")
        if (len(list) == 5):
            lister.append(list)
    #print(lister)

    for i1 in lister:
        if(i1[0]!= 'Filesystem'):
            file.append(i1[0])


            size.append(i1[1])
            used.append((i1[2]))
            avial.append(i1[3])

    return render(request,'task/chart.html', context={'disk': disk, 'data': data,'lister':lister,
                                                      'file':file,'size':size,'used':used,'avial':avial})

def sendemail(request):
    form=Emailform(request.POST)
    if form.is_valid():
        subject = request.POST.get('subject', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        number = request.POST.get('number', '')

    return render(request,'task/email.html',context={'form':form})

def charline(request):
    repeat_cheak_info.delay()
    ret = Used.objects.all()
    print(ret)


    return render(request,'task/chartline.html',context={'ret':ret})


def chartfile(request):
    return render(request,'task/chartfile.html')