from django.shortcuts import render, get_object_or_404 #import를 해줘야 사용 가능
from .models import Blog

# model과 template의 중간자적인 역할을 함. 데이터베이스에 저장된 어떤 데이터가 어떻게 처리될지를 함수로써 정의하고 template으로 출력해줌!

def home(request):#request를 인자로 받음 즉, (home.html을 갖다달라는)request만 들어오면 실행되는 함수 
    blogs = Blog.objects #Blogs안에 있는 객체(objects)를 blogs라는 변수에 담아줄꺼야 
    #.objects:이렇게 하면 model로부터 객체목록을 전달받을 수 있음, 이렇게 전달받은 객체를 --쿼리셋--이라고 함.
    #메소드 : 쿼리셋의 기능들을 처리하거나 정렬할 수 있게끔 해주는 방법중 하나. ex)오름차순 정렬, 없애기, 제목만 출력 등....
    return render(request, 'home.html', {'blogs': blogs})#model의 객체를 담은blogs를 blogs라는 키값에 넣음 ->html상에서 template변수를 통해 출력

    # 퀘리셋과 메소드의 형식
    # 모델이름.퀘리셋(objects).메소드

def detail(request, blog_id):#url을 보면 어떤 정보/인자가 필요한지 알 수 있음 따라서 몇 번 객체를 다룰 것인지에 대한 정보 추가로 필요. 그래서 인자는 두개!
                             #ㄴ즉,request(주세요) blog_id(몇 번 객체를)이라는 뜻 //request에 몇 번째 본문인지 요청이 들어옴
    blog_detail = get_object_or_404(Blog, pk = blog_id)#Blog처럼 모든걸 보여주는게 아니라 특정 번호의 객체만 담아서(그때그때 다른 내용) 보여줘야함 즉 이용자가 원하는 몇 번 블로그객체를 의미
    #get_object_or_404(어떤 클래스, 검색 조건(몇 번 데이터, pk)) : 몇 번 객체를 담아줄것인지를 뜻함 (없으면 뿌셔! 404오류 내보냄)//pk = primary key = 객체들의 이름표, 구분자, 데이터의 대표값,, 어떤 값을 데이터의 대표값으로 삼을지는 정의하기 나름
    return render(request, 'detail.html', {'blog':blog_detail})