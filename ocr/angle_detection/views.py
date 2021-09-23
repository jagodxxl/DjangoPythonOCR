from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE

def button(request):
    return render(request,'home7.html')

def output(request):
    data=requests.get("https://www.google.com/")
    print(data.text)
    data=data.text
    return render(request,'home7.html',{'data':data})

def external(request):
    inp1= request.POST.get('param1')
    inp2= request.POST.get('param2')
    inp4 = inp2 + '/' + inp1
    out= run([sys.executable,'angle_detection/angle_detection.py','-i' + inp4],shell=False,stdout=PIPE)
    print(out)
    return render(request,'home7.html',{'data1':out.stdout.decode('utf-8')})
