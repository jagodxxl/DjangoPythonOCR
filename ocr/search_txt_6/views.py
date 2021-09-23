from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE

def button(request):
    return render(request,'home6.html')

def output(request):
    data=requests.get("https://www.google.com/")
    print(data.text)
    data=data.text
    return render(request,'home6.html',{'data':data})

def external(request):
    inp1= request.POST.get('param1')
    inp2= request.POST.get('param2')
    inp3= request.POST.get('param3')
    inp5= request.POST.get('param4')
    inp4 = inp2 + '/' + inp1
    out= run([sys.executable,'search_txt_6/search_txt_6.py','-i' + inp4,'-t' + inp3,'-s' + inp5],shell=False,stdout=PIPE)
    print(out)
    return render(request,'home6.html',{'data1':out.stdout.decode('utf-8')})
