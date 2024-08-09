from django.urls import path
from django.urls import re_path
from . import views
 
app_name = "articles"
urlpatterns = [
    path('hello/',views.article_list,name='list'),
    path('add/',views.article_add,name = 'add'),
    re_path(r'^(?P<slug>[\w-]+)/$',views.articles_detail,name='detail'),
    

]