# first_app 의 뷰

from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect

articles = {
    'sports': 'Sports Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page'
}

def news_view(request, topic):
    try:
        return HttpResponse(articles[topic])
    # except:
    #     text = 'No page for that topic!'
    #     return HttpResponseNotFound(text)
    except:
        raise Http404('404 Generic Error')



def add_view(request, num1, num2):
    # domain.com/first_app/num1/num2
    return HttpResponse(str(num1+num2))

# 뷰를 요청할 때 마다 호출되는 함수
def sports_view(request):
    return HttpResponse(articles['sports']) # 실제로 템플릿 HTML 파일에 연결. 특정 HTML 파일을 반환한다. JINJA 템플릿을 사용하여 HTML 파일에 내용을 삽입.

def finance_view(request):
    return HttpResponse(articles['finance'])

# first_app 의 urls.py 에 연결
# request 를 받고 HttpResponse("SIMPLE VIEW") 를 반환.


# domain.com/first_app/0 형식이 아닌 domain.com/first_app/sports 형식으로 url
def num_page_view(request, num_page):
    topics_list = list(articles.keys())
    topic = topics_list[num_page]
    return HttpResponseRedirect(topic) # topic으로 redirect를 한다.
