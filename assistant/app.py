from django.shortcuts import render
import requests

def button(request):
    return render(request,'home.html')


def output(request):
    data=requests.get("https://reqres.in/api/user")
    print(data.text)
    data=data.text
    return rander(request,'index.html',{'data':data})