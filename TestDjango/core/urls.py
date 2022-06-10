from django.urls import path 
from .views import home, valida

urlpatterns=[
    path('', home, name="home"),
    path('valida/', valida, name="valida"),
    
]