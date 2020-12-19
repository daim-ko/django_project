#path 함수사용위해 임포트
from django.urls import path
from .views import BookmarkListView, BookmarkCreateView, BookmarkDetailView, BookmarkUpdateView, BookmarkDeleteView

app_name='bookmark'

urlpatterns =[
    path('',BookmarkListView.as_view(), name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'), #view와 bookmark연결
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),
]