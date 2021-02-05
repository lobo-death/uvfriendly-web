from . import views
from django.conf.urls import url

app_name = 'accounts'

urlpatterns = [
    url(r'login/', views.login, name='login'),
    url(r'register/', views.SignUp.as_view(), name='register'),
    url(r'forgot_password/', views.forgot_password, name='forgot_password'),
]