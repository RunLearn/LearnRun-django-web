from django.urls import path

from accountapp.views import account, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('Iam/', account, name = 'account'),

    path('create/',AccountCreateView.as_view(), name = 'create')
]