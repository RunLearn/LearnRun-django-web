from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import account, AccountCreateView, AccountDetailView

app_name = 'accountapp'

urlpatterns = [
    path('Iam/', account, name = 'account'),

    path('login/', LoginView.as_view(template_name='accountapp/login.html'),
         name='login'),

    path('logout/', LogoutView.as_view(template_name='accountapp/logout.html'),
         name='logout'),

    path('create/',AccountCreateView.as_view(), name = 'create'),
    path('detail/<int:pk>',AccountDetailView.as_view(), name = 'detail')
]