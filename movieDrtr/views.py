from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
import random
import os
import shutil
import sys
import urllib.request
import urllib.parse
import bs4
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from myshaman import settings

from rest_framework import viewsets
from rest_framework.decorators import action
from .serializers import DirectorInfoSerializer
from .models import DirectorInfo

class directorInfoView(viewsets.ModelViewSet):
    queryset = DirectorInfo.objects.all()
    serializer_class = DirectorInfoSerializer

    @action(detail=False)
    # list_route기능은 detail=false로 수용됨. 이렇게 하면 기본 url에 method명을 넣어서 get요청할 시,
    # 추가적인 작업이 가능. 아래는 임시로 이미지를 받아온 폴더를 삭제하는 작업
    def clearTempImage(self, request):
        shutil.rmtree(f"{settings.BASE_DIR}/tempImage")
        return HttpResponse("folder removed.")

class apiView(View):
    
    def get(self, request):
        try:
            client_id = "YcZ9Mf8_Bi7egqB3xNLO"
            client_secret = "PBW5ffxhRR"
            encText = urllib.parse.quote("기생충")
            url = "https://openapi.naver.com/v1/search/movie.json?query=" + encText # json 결과
            # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
            request = urllib.request.Request(url)
            request.add_header("X-Naver-Client-Id",client_id)
            request.add_header("X-Naver-Client-Secret",client_secret)
            response = urllib.request.urlopen(request)
            rescode = response.getcode()
            if(rescode==200):
                response_body = response.read()
                print(response_body.decode('utf-8'))
                return HttpResponse(response_body.decode('utf-8'))
            else:
                print("Error Code:" + rescode)                    
            
        except:
            return HttpResponse(status=504,)

class getPeopleView(View):
    
    def get(self, request):
        try:
            searchDtr = request.GET.get('searchDrt')
            encText = urllib.parse.quote(searchDtr)
            # encText = urllib.parse.quote("스티븐스필버그")
            url = f'https://movie.naver.com/movie/search/result.nhn?query={encText}&section=people&ie=utf8'
            html = urllib.request.urlopen(url)
            bsObj = bs4.BeautifulSoup(html, "html.parser")
            people = bsObj.select_one("ul.search_list_1>li>dl>dt>a")['href']
            peopleCode = int(people.split('=')[-1])
            if(type(peopleCode)==int):
                return HttpResponse(peopleCode)
            else:
                print("Error Code:" + peopleCode)                    

        except:
            return HttpResponse(status=503,data='No matched data')

class getPeopleListView(View):
    
    def get(self, request):
        try:
            # 네이버영화에서 PEOPLE CODE 받아오기
            searchDtr = request.GET.get('searchDrt')
            encText = urllib.parse.quote(searchDtr)
            # encText = urllib.parse.quote("스티븐스필버그")
            url = f'https://movie.naver.com/movie/search/result.nhn?query={encText}&section=people&ie=utf8'
            html = urllib.request.urlopen(url)
            bsObj = bs4.BeautifulSoup(html, "html.parser")
            peopleLists = bsObj.select("ul.search_list_1>li")
            peopleCode = 0
            for i in range(len(peopleLists)):
                element = peopleLists[i]
                tempText = element.get_text()
                searchResult = tempText.find("감독")
                if (searchResult != -1):
                    peopleCode = int(element.select_one("dl>dt>a")['href'].split('=')[-1])

            # 임시로 사용할 이미지 다운 받기
            BASE = settings.BASE_DIR
            outpath = f'{BASE}/tempImage'
            if not os.path.isdir(outpath):
                os.makedirs(outpath)
            ranNum = random.randint(1, 5000)
            urllib.request.urlretrieve(f'https://mdl.artvee.com/ft/1{ranNum}po.jpg', f'{outpath}/{peopleCode}.jpg')
            
            return HttpResponse(peopleCode)

        except:
            return HttpResponse(status=503,data='No matched data')

# https://movie.naver.com/movie/bi/pi/filmoMission.nhn?peopleCode=9479&year=0

