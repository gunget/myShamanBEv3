from django.db import models

# Create your models here.

class DirectorInfo(models.Model):
    name = models.CharField(max_length=100, default='')
    peopleCode = models.IntegerField()
    image = models.ImageField(upload_to='media/%Y/%m/%d', default='media/no_img.png', blank=True, null=True)
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
    name = models.CharField(max_length=100, default='')
    peopleCode = models.IntegerField()
    job = models.CharField(max_length=100, default='', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    #글이 추가될 때 자동으로 날짜가 입력됨
       
    class Meta:#필드속성 외에 필요한 테이블의 파라미터를 정의하기 위해, 내부클래스 선언(이또한 상속받는 것)
        ordering = ['name'] #모델객체의 리스트 출력시 이름순(오름차순)으로 정렬
        #오름차순(ascending)은 순방향(일반적인 사용법 대로. 1-2-3, ㄱ-ㄴ-ㄷ, a-b-c). 오룸-일반(모두 ㅇ)
        #내림차순(descending)은 역방향(일반적인 사용법과 반대)

    def __str__(self):
        return self.name #어디서는 directorInfo테이블의 객체를 호출하면, 그 객체의 title값을 표시하라. 단, __str__을 적용해 문자형태로 알기쉽게 표기



# keyword = str(input('검색어는? ='))
# #네이버에서 검색할때 처럼 두가지이상의 키워드를 동시에 넣어도 &검색 된다.
# displayNumber = str(input('검색할 기사 수는? ='))
# def news_search(min_name): #네이버 뉴스검색 API사용하는 함수
#     encText = urllib.parse.quote(min_name)
#     # 한글등 non-ASCII text를 URL에 넣을 수 있도록 "%" followed by hexadecimal digits 로 변경
#     # URL은 ASCII 인코딩셋만 지원하기 때문임
#     url = "https://openapi.naver.com/v1/search/news.json?query=" + encText + "&display="+ displayNumber + "&sort=sim"
#     request = urllib.request.Request(url) #urlopen클래스에 쓸 request object만들기
#     # urllib.request.Request()는 HTTP Header 변경시에 사용함
#     # 네이버에서도 다음 HTTP Header 키를 변경해야하기 때문에 사용함
#     # HTTP Header 변경이 필요없다면, 바로 urllib.request.urlopen()함수만 사용해도 됨
#     request.add_header("X-Naver-Client-Id", id) #만들어진 requset object에 헤더 붙이기
#     request.add_header("X-Naver-Client-secret", secret)

#     reponse = urllib.request.urlopen(request) # request object를 서버에 보내고 응답을 받아서 reponse 변수에 저장
#     rescode = reponse.getcode()
#     # getcode() 메서드로 HTTP '응답 상태 코드'를 가져올 수 있음
#     # HTTP 요청에 대한 정상응답일 경우, HTTP 응답 상태 코드 값이 200이 됩니다.
#     # HTTP 요청 응답이 정상적일 경우, 해당 HTML 데이터를 수신되었기 때문에 필요한 데이터 추출이 가능함
#     if (rescode == 200):
#         reponse_body_str = reponse.read().decode('utf-8')
#         # json_acceptable_string = reponse_body_str.replace("'","\"")
#         reponse_body = json.loads(reponse_body_str)
#         # 응답값을 읽으면 json형태로 표시가 되어 알아볼순 있지만 후처리 불가능. json.load()모듈을 사용해 이를 딕셔너리로
#         # 바꿔서 파일 추출등 후처리 가능
#         title_link = {}
#         for i in range(len(reponse_body['items'])): #item이 검색 결과가 나오는 부분
#             title_link[reponse_body['items'][i]['title']] = reponse_body['items'][i]['link']
#             #{타이틀:링크, 타이틀2:링크2}형식으로 반환받는 방법
#         return title_link
#     else:
#         print("Error Code" + rescode)

# result = news_search(keyword)

# def save_to_html(search_result, cur_keyword): #검색한 결과를 별도의 html파일로 저장하는 방법
#     with open(cur_keyword+'.html', 'w', encoding='UTF-8') as file:
#         for k in search_result.keys():
#             file.write("<a href="+search_result[k]+">"+k+"<a>"+"<br></br>")

# save = save_to_html(result, keyword)

# #name = re.search("(?<=>).*(?=<)", source)  '<b>김연아<b>'에서 김연아만 따 내기 위한 정규문. 후방긍정, 전방긍정