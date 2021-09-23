from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE

def button(request):
    return render(request,'home2.html')

def output(request):
    data=requests.get("https://www.google.com/")
    print(data.text)
    data=data.text
    return render(request,'home2.html',{'data':data})

def external(request):
    inp1= request.POST.get('param1')
    inp2= request.POST.get('param2')
    inp3= request.POST.get('param3')
    out= run([sys.executable,'ocr_core/ocr_core3.py',inp1,inp2,inp3],shell=False,stdout=PIPE)
    print(out)
    return render(request,'home2.html',{'data1':out.stdout.decode('utf-8')})
