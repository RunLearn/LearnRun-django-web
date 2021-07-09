from django.urls import path

from accountapp.views import account

app_name = 'accountapp'

urlpatterns = [
    path('Iam/', account, name = 'account')
]