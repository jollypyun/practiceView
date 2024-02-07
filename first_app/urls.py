from django.urls import path
from . import views # 뷰에 연결하기 위함.


# 리스트 내부에 경로를 추가한다.
# domain.com/first_app/
urlpatterns = [
    # 경로는 문자열이여야 한다. 빈 문자열이여도 상관없다. 다만, 빈 문자열이 home을 뜻하는 것은 아니다.
    # 프로젝트 레벨의 urls.py 파일에서 실제로 이러한 뷰가 무엇에 해당하는지 정의를 하기 때문이다.

    # 새 뷰를 만들면 새로운 url
    # path('sports/', views.sports_view),
    # path('finance/', views.finance_view)

    # 원하는 주제인 topci을 news_view에 건네면 articles에 그에 따른 값을 찾는다. 패턴을 topic을 이용하여 동적으로 정의 (<> 이용)
    path('<str:topic>/', views.news_view), # 경로 변환기를 이용하여 str 타입만 변수로 받음.
    # path('<int:num1>/<int:num2>', views.add_view),


    # num_page_view 와 연결되고
    path('<int:num_page>', views.num_page_view)
]

# 경로 변환기에 관한 자료 찾기