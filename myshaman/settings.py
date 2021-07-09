
from pathlib import Path
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# import local_setting
import datetime

import mimetypes
import dj_database_url # 최상단에 선언부분에 입력



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '-n%sr$4btonoo6!!q_+_9e4&*wsn$av4)77-t^o)m_*3m8@=4t')
# 출처: https://zodlab.tistory.com/95 [조드군의 일상]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get('DJANGO_DEBUG', False))

# ALLOWED_HOSTS = ['*'] #조드군의 일상에선 이렇게 하라고함
ALLOWED_HOSTS = ['myshaman.herokuapp.com']
# ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
    'allauth.socialaccount',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages', 
    'django.contrib.staticfiles', 
    #사용자 앱에서 쓰는 static파일들을 매핑해주는 앱이 staticfiles
    'movieDrtr.apps.MoviedrtrConfig',
]

SITE_ID = 1

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
    ),
}

JWT_AUTH = {
    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_ALGORITHM': 'HS256',
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=3),
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=1),
}

# JWT_SECRET_KEY: JWT의 비밀키(Secret Key)로 어떤걸 사용할지 작성합니다. 여기에서는 장고(django)와 같은 비밀키를 사용하였지만 사용할 때는 다른 키를 사용하시길 권장.
# JWT_ALGORITHM: JWT 암호화에 사용되는 알고리즘을 지정.
# JWT_ALLOW_REFRESH: JWT 토큰을 갱신할 수 있게 할지 여부를 결정.
# JWT_EXPIRATION_DELTA: JWT 토큰의 유효 기간을 설정.
# JWT_REFRESH_EXPIRATION_DELTA: JWT 토큰 갱신의 유효기간.
# JWT_EXPIRATION_DELTA와 JWT_REFRESH_EXPIRATION_DELTA이 잘 이해가 되지 않는데요. 위와 같이 설정한 경우 JWT 토큰을 7일 안에 갱신하지 않으면 JWT 토큰을 사용할 수 없고 로그아웃됩니다. 또한 7일안에 열심히 갱신해도 28일 후에는 갱신할 수 없습니다. 즉, 열심히 갱신해도 28일 후에는 로그아웃 처리가 되는 것을 의미.

#ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_REQUIRED = False
#ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_VERIFICATION = "none"
REST_USE_JWT = True
ACCOUNT_LOGOUT_ON_GET = True

# LOGIN_REDIRECT_URL = '/main/'

ROOT_URLCONF = 'myshaman.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'myshaman', 'build')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myshaman.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
db_from_env = dj_database_url.config(conn_max_age=500) # DB 설정부분 아래에 입력
DATABASES['default'].update(db_from_env)
#기본 db인 sqlite3를 heroku전용인 postgreSQL로 바꾸는 설정

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ko-kr'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False
# USE_TZ = True


# Static files (CSS, JavaScript, Images)
# staticfiles라는 기본 앱이 사용하는 설정
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
#장고 템플릿에서 static태그를 사용할 때 이 경로를 이용하여 절대경로로 치환한다.
#템플릿을 사용하지 않는 리액트 프론트에서는 특별히 관계없는 설정

# STATIC_ROOT = os.path.join(BASE_DIR, 'myshaman', 'build', 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# 아파치, nginx등 웹서버가 클라이언트에 static file을 제공해주려면, 파일들이 어디있는지
# 알아야 한다. 이를 위해 collectstatic명령어로 파일을 모아 특정 폴더에 몰아넣는데,
# 이때 사용하는 폴더가 Static_Root폴더. collectStatic명령어는 폴더를 만들지 않는다.
# 반드시 미리 만들어져 있어야 함

# staticfiles 기본앱이 프로젝트에서 사용되는 static파일들을 가져올때 사용하는 경로
# react를 프론트로 쓸 경우 build/static경로를 찾아서 엮어주면 된다.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'myshaman', 'build', 'static'),
] 

# STATICFILES_STORAGE = [ ] 외부에 STATIC파일용 서버를 별도로 둘 경우 설정 필요


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') #사용자가 업로드한 파일 관리

CORS_ORIGIN_WHITELIST = ['https://myshaman.herokuapp.com', ] 
# CORS_ORIGIN_WHITELIST = ( 'http://localhost:3000', 'http://127.0.0.1:3000', 'http://localhost:8000', 'http://127.0.0.1:8000' )
CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True

mimetypes.add_type("text/javascript", ".js", True)