# fro m django.http import HttpResponse
from django.shortcuts import render
def homepage(resquest):
    return render(resquest,'home.html');
    # return HttpResponse('Hello iboytch is here');

def about(resquest):
    return render(resquest,'about.html');
    # return HttpResponse('About iboytech');