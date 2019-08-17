from django.contrib import admin
from .models import Blog #from같은 폴더 안에 있는 model안에서..Blog객체를 가져와라
#model에서 작성한 내용을 적어줘야 /admin사이트에서 model에 적은 데이터를 볼 수 있음 ex)Blog
admin.site.register(Blog) #admin 사이트에 blog등록해라