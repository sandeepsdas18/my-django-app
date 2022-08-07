from django.urls import path, re_path
from capital_city import views
#from homepage import views

urlpatterns = [
    path("", views.capital, name='capital')
]