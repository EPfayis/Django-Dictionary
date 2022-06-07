from http.client import HTTPResponse
from datetime import datetime
import requests
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from .models import TblSearchCount


class Dict(APIView):

    def get(self, request):
        word = request.GET["word"]
        print("request accepted.")

        objSearchCount = TblSearchCount()
        objSearchCount.word = word
        objSearchCount.date = datetime.now().date()
        objSearchCount.save()
        print("search count added")

        res = requests.get("https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=ml&dt=t&q=" + word)

        return JsonResponse({"meaning":res.json()[0][0][0]})


class Count(APIView):

    def get(self, request):

        dic = {}

        qs = TblSearchCount.objects.filter(date=datetime.now().date())

        for obj in qs:
            if obj.word not in dic.keys():
                dic[obj.word] = 1
            else:
                dic[obj.word] = dic[obj.word] + 1
            # Calculated the count of each word and stored in a dictionary

        dic = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1], reverse=True)}
        # Sorted the dictionary by number of searches descending

        return JsonResponse(dic)


class DicTemplate(APIView):

    def get(self,request):

        dicContent = {
            "meaning" : "",
            "topSearch" : {},
        }

        word = request.GET.get("word","")
        dicContent["word"] = word

        if word != "":
            meaning = requests.get("http://127.0.0.1:8000/dict/?word=" + word).json()
            dicContent["meaning"] = meaning["meaning"]

        topSearch = requests.get("http://127.0.0.1:8000/dict/count").json()
        dicContent["topSearch"] = topSearch


        return render(request, "dictionary.html",dicContent)