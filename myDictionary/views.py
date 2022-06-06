from http.client import HTTPResponse
from datetime import datetime
import requests
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from .models import TblSearchCount

class Dict(APIView):

    def get(self,request):

        word = request.GET["word"]
        print("request accepted.")

        objSearchCount = TblSearchCount()
        objSearchCount.word = word
        objSearchCount.date = datetime.now().date()
        objSearchCount.save()
        print("search count added")

        res = requests.get("https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=ml&dt=t&q="+word)

        return HttpResponse(res.json()[0][0][0])

class Count(APIView):

    def get(self,request):

        dic = {}

        qs = TblSearchCount.objects.filter(date= datetime.now().date())

        for obj in qs:
            if obj.word not in dic.keys():
                dic[obj.word] = 1
            else:
                dic[obj.word] = dic[obj.word] + 1

        dic = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1], reverse= True)}

        return JsonResponse(dic)


