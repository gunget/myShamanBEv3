from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DirectorInfo(models.Model):
    owner = models.ForeignKey(User, related_name='directorInfo', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='')
    peopleCode = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    # image = models.ImageField(upload_to='media/%Y/%m/%d', default='media/no_img.png', blank=True, null=True)
    # image upload시 사용. serializer에도 설정해줘야 함
    wisesaying = models.CharField(max_length=300, default='')
    created_date = models.DateTimeField(auto_now_add=True)
    #글이 추가될 때 자동으로 날짜가 입력됨
       
    class Meta:#필드속성 외에 필요한 테이블의 파라미터를 정의하기 위해, 내부클래스 선언(이또한 상속받는 것)
        ordering = ['name'] #모델객체의 리스트 출력시 이름순(오름차순)으로 정렬
        #오름차순(ascending)은 순방향(일반적인 사용법 대로. 1-2-3, ㄱ-ㄴ-ㄷ, a-b-c). 오룸-일반(모두 ㅇ)
        #내림차순(descending)은 역방향(일반적인 사용법과 반대)

    def __str__(self):
        return self.name #어디서는 directorInfo테이블의 객체를 호출하면, 그 객체의 title값을 표시하라. 단, __str__을 적용해 문자형태로 알기쉽게 표기

class FicWriterInfo(models.Model):
    owner = models.ForeignKey(User, related_name='ficWriterInfo', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='')
    peopleCode = models.IntegerField()
    job = models.CharField(max_length=100, default='', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
       
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class NonFicWriterInfo(models.Model):
    owner = models.ForeignKey(User, related_name='nonFicWriterInfo', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='')
    peopleCode = models.IntegerField()
    job = models.CharField(max_length=100, default='', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
       
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class OthersInfo(models.Model):
    owner = models.ForeignKey(User, related_name='othersInfo', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='')
    job = models.CharField(max_length=100, default='', blank=True, null=True)
    description = models.CharField(max_length=500, default='', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
       
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


