"""myshaman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from movieDrtr.views import apiView, getPeopleListViewMV, getPeopleListViewFT, UserListView, ReactAppView
from rest_framework import routers
from movieDrtr import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

route = routers.DefaultRouter()
route.register('directorInfo', views.directorInfoView, 'DirectorInfo')
route.register('ficWriterInfo', views.ficWriterInfoView, 'FicWriterInfo')
route.register('nonFicWriterInfo', views.NonficWriterInfoView, 'NonFicWriterInfo')
route.register('othersInfo', views.OthersInfoView, 'OthersInfo')
# DefaultRouter를 쓰면 기본 url(여기선 directorInfo) 뒤에 다른 url을 써도 알아서 루팅해줌
# 보통 viewset을 이용할때 @action을 써서 메소드를 추가하면 '기본url/메소드명'으로 호출시
# 해당 메소드가 실행되게 된다.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),
    path('search/', apiView.as_view(), name='search'),
    path('getPpMovie/', getPeopleListViewMV.as_view(), name='getPp'),
    path('getPpWriter/', getPeopleListViewFT.as_view(), name='getPpFT'),
    path('users/', views.UserListView.as_view()),

    path("rest-auth/", include('rest_auth.urls')),
    path("rest-auth/registration/", include('rest_auth.registration.urls')),

    path('api-jwt-auth/', obtain_jwt_token),          # JWT 토큰 획득
    path('api-jwt-auth/refresh/', refresh_jwt_token), # JWT 토큰 갱신
    path('api-jwt-auth/verify/', verify_jwt_token),   # JWT 토큰 확인

    # React담당해야하는 FrontEnd Urls
    re_path(r'^(?:.*)/?$', views.ReactAppView.as_view()), #그외 모든 url을 리액트가 처리
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
