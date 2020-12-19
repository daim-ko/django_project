from django.shortcuts import render
#여기서 정의할 북마크리스트뷰는 이걸 상속받아 만들어진다.
from django.views.generic.list import ListView
#모델스에 정리한 북마크 모델을 가져온다.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Bookmark
from django.urls import reverse_lazy


# Create your views here.
class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('bookmark:list')
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model= Bookmark
    fields= ['site_name', 'url']
    template_name_suffix= '_update'

class BookmarkDeleteView(DeleteView):
    model= Bookmark
    success_url = reverse_lazy('bookmark:list')


