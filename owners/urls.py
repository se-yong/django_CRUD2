from django.urls import path

from owners.views import OwnerView

urlpatterns = [
    path('', OwnerView.as_view()) 
]
## 앞단에서 작성한 crud2-urls.py dp 내용을 잘 작성만해주면 
## path ''이 의미하는것은 앞단의 urls.py(crud2) 에 통하는 모든신호들을 받을수있다라는것을의미
# 
# 
# 
# 에러가 발생한 이유 owners.py에 클래스명을 OwnersView 라고 입력해서 오류남
# views.py 에 클래스명과 이곳에 적어준 클래스명이 다르기때문에 오류발생함
# 오류 메세지 : ImportError: cannot import name 'OwnersView' from 'owners.views' (/mnt/c/Users/Se-yong.park/wecode/crud2/owners/views.py) 
# -> urls.py 에 클래스명을 수정하니 해결함  
# OwnersView -> OwnerView