from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE

def button(request):
    return render(request,'home.html')

def output(request):
    data=requests.get("https://www.google.com/")
    print(data.text)
    data=data.text
    return render(request,'home.html',{'data':data})

def external(request):
    inp1= request.POST.get('param1')
    inp2= request.POST.get('param2')
    out= run([sys.executable,'pdf2jpg/pdf2jpg.py',inp1,inp2],shell=False,stdout=PIPE)
    print(out)
    return render(request,'home.html',{'data1':out.stdout.decode('utf-8')})
