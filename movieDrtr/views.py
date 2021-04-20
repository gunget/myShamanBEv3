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
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.decorators import action
from .serializers import DirectorInfoSerializer, FicWriterInfoSerializer, NonFicWriterInfoSerializer, OthersInfoSerializer, UserSerializer
from .models import DirectorInfo, FicWriterInfo, NonFicWriterInfo, OthersInfo

from django.contrib.auth.models import User

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class directorInfoView(viewsets.ModelViewSet):
    queryset = DirectorInfo.objects.all()
    serializer_class = DirectorInfoSerializer
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=False)
    # list_route기능은 detail=false로 수용됨. 이렇게 하면 기본 url에 method명을 넣어서 get요청할 시,
    # 추가적인 작업이 가능. 아래는 임시로 이미지를 받아온 폴더를 삭제하는 작업
    def clearTempImage(self, request):
        shutil.rmtree(f"{settings.BASE_DIR}/tempImage")
        return HttpResponse("folder removed.")

class ficWriterInfoView(viewsets.ModelViewSet):
    queryset = FicWriterInfo.objects.all()
    serializer_class = FicWriterInfoSerializer
    permission_classes = [IsAuthenticated,]    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class NonficWriterInfoView(viewsets.ModelViewSet):
    queryset = NonFicWriterInfo.objects.all()
    serializer_class = NonFicWriterInfoSerializer
    permission_classes = [IsAuthenticated,]    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class OthersInfoView(viewsets.ModelViewSet):
    queryset = OthersInfo.objects.all()
    serializer_class = OthersInfoSerializer
    permission_classes = [IsAuthenticated,]    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

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

class getPeopleListViewMV(View):
    
    def get(self, request):
        try:
            # 네이버영화에서 PEOPLE CODE 받아오기
            searchDtr = request.GET.get('searchDrt')
            encText = urllib.parse.quote(searchDtr)
            url = f'https://movie.naver.com/movie/search/result.nhn?query={encText}&section=people&ie=utf8'
            html = urllib.request.urlopen(url)
            bsObj = bs4.BeautifulSoup(html, "html.parser")
            peopleLists = bsObj.select("ul.search_list_1>li")
            peopleCode = 0
            for i in range(len(peopleLists)):
                element = peopleLists[i]
                tempText = element.get_text() #모든 엘러먼트의 텍스트만 전부 골라서 받아짐
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

class getPeopleListViewFT(View):
    
    def get(self, request):
        try:
            # 네이버검색에서 PEOPLE CODE 받아오기
            searchWtr = request.GET.get('searchWtr')
            jobs0 = request.GET.get('jobs[0]')
            jobs1 = request.GET.get('jobs[1]')
            jobs2 = request.GET.get('jobs[2]')
            encText = urllib.parse.quote(searchWtr)
            url = f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={encText}"
            html = urllib.request.urlopen(url)
            bsObj = bs4.BeautifulSoup(html, "html.parser")
            peopleLists = bsObj.select("section#people_info_z div.same_people ul li")
            peopleCode = 0
            if peopleLists :
                for i in range(len(peopleLists)):
                    element = peopleLists[i]
                    tempText = element.get_text()
                    searchResult = tempText.find(jobs0)
                    searchResult2 = tempText.find(jobs1)
                    searchResult3 = tempText.find(jobs2)
                    if (searchResult != -1) or (searchResult2 != -1) or (searchResult3 != -1):
                        tempList = peopleLists[0].select_one("div.same_con a")['href']
                        peopleCode = tempList.split('&os=')[-1].split('&')[0]
            else:
                peopleCode = int(bsObj.select_one("section#people_info_z dd.name > a")['href'].split('=')[-1])

            return HttpResponse(peopleCode)

        except:
            return HttpResponse(status=503,data='No matched data')
