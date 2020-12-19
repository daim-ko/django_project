#강의 보면서 작성한 것 polls밑에 urls를 만들어서 작성함
from django.urls import path
from . import views

app_name= 'polls'

urlpatterns = [
    #ex: /polls/
    path('', views.IndexView.as_view() , name='index'),
    #ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #ex: /polls/5/results.
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote')

]