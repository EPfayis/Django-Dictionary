from http.client import HTTPResponse
import requests
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse

class Dict(APIView):

    def get(self,request):

        word = request.GET["word"]

        res = requests.get("https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=ml&dt=t&q="+word)

        print(res.json()[0][0][0])

        return HttpResponse(res.json()[0][0][0])


