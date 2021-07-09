from django.shortcuts import render
from django.http import HttpResponse

def account(request):
    if request.method == "POST":
        return render(request, 'accountapp/base.html',
                      context={'text': 'POST METHOD!'})
    else:
        return render(request, 'accountapp/base.html',
                      context={'text': 'GET METHOD!'})
