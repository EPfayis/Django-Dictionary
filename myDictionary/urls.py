from django.urls import path
from .views import Dict, Count

urlpatterns = [
    path('', Dict.as_view(), name= "dict"),
    path('count/', Count.as_view(), name= "count"),
]