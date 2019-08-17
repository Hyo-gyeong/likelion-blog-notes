"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
#request는 url을타고 장고로 들어옴.
from django.contrib import admin
from django.urls import path
import blogapp.views  #blogapp앱 안에 있는 views를 가져와라

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name="home"), #blogapp이라는 앱안에 있는 views안에 있는 home이라는 파일 가져오는데 이름은home
    path('blog/<int:blog_id>', blogapp.views.detail, name="detail"),#path 함수는 url이름, 함수이름, path이름 이렇게 3개의 인자를 받음 & blog_id: 두번째인자로 받은 detail함수에게 넘겨지는 인자, 이용자와 직접 상호 작용을 하는 메시지 역할을 하는 url을 통해 두번째 인자를 detail에게 전달
    #path converter사용 방법: <type:변수이름>, type= int, str, uuid.../ 여러 객체들을 다루는 계층적인 url을 자동생성할 때 좋음
]