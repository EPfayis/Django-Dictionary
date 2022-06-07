from django.urls import path
from .views import Dict, Count, DicTemplate

urlpatterns = [
    path('', Dict.as_view(), name= "dict"),
    path('count/', Count.as_view(), name= "count"),
    path('template/', DicTemplate.as_view(), name= "template"),
]