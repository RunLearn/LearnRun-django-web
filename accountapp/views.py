from django.shortcuts import render
from django.http import HttpResponse

from accountapp.models import NewModel


def account(request):
    if request.method == "POST":

        temp =request.POST.get('input_text')
        new_model = NewModel()
        new_model.text = temp
        new_model.save()

        return render(request, 'accountapp/base.html',
                      context={'new_model' : new_model})
    else:
        return render(request, 'accountapp/base.html',
                      context={'text': 'GET METHOD!'})
