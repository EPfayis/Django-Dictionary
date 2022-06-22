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

        objSearchCount = TblSearchCount.objects.filter(word__iexact= word).filter(date= datetime.now().date())
        if objSearchCount.count() == 0:
            objSearchCount = TblSearchCount()
            objSearchCount.date = datetime.now().date()
            objSearchCount.word = word
            objSearchCount.count = 1

        else:
            objSearchCount = objSearchCount.first()
            objSearchCount.count = objSearchCount.count + 1

        objSearchCount.save()
        print("search count added")

        res = requests.get("https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=ml&dt=t&q=" + word)

        return JsonResponse({"meaning":res.json()[0][0][0]})


class Count(APIView):

    def get(self, request):

        dic = {}

        qs = TblSearchCount.objects.filter(date=datetime.now().date()).order_by("-count")

        for c,obj in enumerate(qs):
            if c == 3:
                break

            dic[obj.word] = obj.count


        return JsonResponse(dic)


class DicTemplate(APIView):

    def get(self,request):
        try:

            dicContent = {
                "meaning" : "",
                "topSearch" : {},
            }

            word = request.GET.get("word","")
            dicContent["word"] = word
            print("request accepted")

            if word != "":
                meaning = requests.get("http://127.0.0.1:8000/dict/?word=" + word).json()
                dicContent["meaning"] = meaning["meaning"]
                print("meaning fetched")

            topSearch = requests.get("http://127.0.0.1:8000/dict/count").json()
            dicContent["topSearch"] = topSearch
            print("top search optained")

            return render(request, "dictionary.html",dicContent)
        except Exception as e:
            return JsonResponse({"error" : str(e)})