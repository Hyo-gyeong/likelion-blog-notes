from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 100)#title이라는 변수 안에 model안에 있는 (character field)문자로 되어있는 데이터(좀 짧은애들)를 title이라는 변수로 정의하겠다. 최대 길이는 200로 지정 
    pub_date = models.DateTimeField('date published')#DateTimeField = 날짜와 시간을 나타내는 데이터를 publish date로 처리해주겠다 (publish된 날짜로)
    body = models.TextField()#긴 문자열 = textfield
    #->이렇게 정의한 데이터는 admin사이트 Blog +Add에서 볼 수 있음!
    def sum(self):
        return self.body[:100] #본문 100글자씩만 보여줘!

    #models.뭐뭐뭐field(추가적) 이런 형식 정형화되어있음//정리해준 자료 참고..!
    #모델에 작성한 데이터를 데이터베이스가 알아듣게끔하고 적용시켜주어야 함. 이유:데이터베이스와 장고는 별개의 것이니까
    # = makemigration(migration파일 만들기) migrate(적용)
    def __str__(self):
        return self.title#admin사이트에서 쓴 글은 blog object(1)로 보여주는게 아니라 내가 작성한 제목으로 보여주고 싶을 때