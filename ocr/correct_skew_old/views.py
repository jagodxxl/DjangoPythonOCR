from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE

def button(request):
    return render(request,'home3.html')

def output(request):
    data=requests.get("https://www.google.com/")
    print(data.text)
    data=data.text
    return render(request,'home3.html',{'data':data})

def external(request):
    inp0= '--image'
    inp1= request.POST.get('param1')
    inp2= request.POST.get('param2')
    inp3= inp2 + '/' + inp1
    out= run([sys.executable,'correct_skew_old/correct_skew_old.py',inp0,inp3],shell=False,stdout=PIPE)
    print(out)
    return render(request,'home3.html',{'data1':out.stdout.decode('utf-8')})
